import os
import json
import sys
from typing import Callable, Dict, TypedDict, List, Any, Optional
import logging

from academic_metrics.core import (
    CategoryProcessor,
    FacultyPostprocessor,
)
from academic_metrics.orchestrators import (
    CategoryDataOrchestrator,
    ClassificationOrchestrator,
)
from academic_metrics.data_collection import CrossrefWrapper, Scraper
from academic_metrics.utils import (
    ClassifierFactory,
    WarningManager,
    Taxonomy,
    Utilities,
    APIKeyValidator,
)
from academic_metrics.enums import AttributeTypes
from academic_metrics.factories import DataClassFactory
from academic_metrics.strategies import StrategyFactory
from academic_metrics.DB import DatabaseWrapper

from academic_metrics.constants import (
    INPUT_FILES_DIR_PATH,
    SPLIT_FILES_DIR_PATH,
    OUTPUT_FILES_DIR_PATH,
    LOG_DIR_PATH,
)


class SaveOfflineKwargs(TypedDict):
    offline: bool
    run_crossref_before_file_load: bool
    make_files: bool
    extend: bool


class PipelineRunner:
    SAVE_OFFLINE_KWARGS: SaveOfflineKwargs = {
        "offline": False,
        "run_crossref_before_file_load": False,
        "make_files": False,
        "extend": False,
    }

    def __init__(
        self,
        ai_api_key: str,
        crossref_affiliation: str,
        data_from_year: int,
        data_to_year: int,
        mongodb_url: str,
        db_name: str = "Site_Data",
        debug: bool = False,
    ):
        # Set up pipeline-wide logger
        self.log_file_path = os.path.join(LOG_DIR_PATH, "pipeline.log")
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        self.logger.handlers = []
        if not self.logger.handlers:
            # Create file handler
            handler = logging.FileHandler(self.log_file_path)
            handler.setLevel(logging.ERROR)
            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.DEBUG)
            console_formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )
            console_handler.setFormatter(console_formatter)
            self.logger.addHandler(console_handler)

        self.logger.info("Initializing PipelineRunner")

        self.ai_api_key = ai_api_key
        self.db_name = db_name
        self.mongodb_url = mongodb_url
        self.db = self._create_db()
        self.scraper = self._create_scraper()
        self.crossref_wrapper = self._create_crossref_wrapper(
            affiliation=crossref_affiliation,
            from_year=data_from_year,
            to_year=data_to_year,
        )
        self.taxonomy = self._create_taxonomy()
        self.warning_manager = self._create_warning_manager()
        self.strategy_factory = self._create_strategy_factory()
        self.utilities = self._create_utilities_instance()
        self.classification_orchestrator = self._create_classification_orchestrator()
        self.dataclass_factory = self._create_dataclass_factory()
        self.category_processor = self._create_category_processor()
        self.faculty_postprocessor = self._create_faculty_postprocessor()
        self.debug = debug
        self.logger.info("PipelineRunner initialized successfully")

    def run_pipeline(
        self, save_offline_kwargs: SaveOfflineKwargs = SAVE_OFFLINE_KWARGS
    ):
        # Get the existing DOIs from the database
        # so that we don't process duplicates
        existing_dois = self.db.get_dois()
        self.logger.info(f"Found {len(existing_dois)} existing DOIs in database")

        # Get data from crossref for the school and date range
        data: List[Dict[str, Any]] = []
        if save_offline_kwargs["offline"]:
            if save_offline_kwargs["run_crossref_before_file_load"]:
                data = self.crossref_wrapper.run_all_process()
            if save_offline_kwargs["make_files"]:
                self._make_files()
            data = self._load_files()
        else:
            # Set this to true once database is integrated
            # save_to_db = True
            data = self.crossref_wrapper.run_all_process()

        # Filter out articles whose DOIs are already in the db or those that are not found
        already_existing_count = 0
        filtered_data = []
        for article in data:
            # Get the DOI out of the article item
            attribute_results = self.utilities.get_attributes(
                article, [AttributeTypes.CROSSREF_DOI]
            )
            # Unpack the DOI from the dict returned by get_attributes
            doi = attribute_results[AttributeTypes.CROSSREF_DOI]
            # Only keep articles that have a DOI and aren't already in the database
            if doi[0] and doi[1] not in existing_dois:
                filtered_data.append(article)
            else:
                already_existing_count += 1

        self.logger.info(f"Filtered out {already_existing_count} articles")

        data = filtered_data

        self.logger.info(f"\n\nDATA: {data}\n\n")
        self.logger.info("=" * 80)
        if self.debug:
            print(f"There are {len(data)} articles to process.")
            response = input("Would you like to slice the data? (y/n)")
            if response == "y":
                res = input("How many articles would you like to process?")
                data = data[: int(res)]
                self.logger.info(f"\n\nSLICED DATA:\n{data}\n\n")

        self.logger.info("=" * 80)
        # Run classification on all data
        # comment out to run without AI for testing
        self.logger.info(f"\n\nRUNNING CLASSIFICATION\n\n")
        data = self.classification_orchestrator.run_classification(data)

        # Process classified data and generate category statistics
        category_orchestrator = self._create_orchestrator(
            data=data, extend=save_offline_kwargs["extend"]
        )
        category_orchestrator.run_orchestrator()

        # Get all the processed data from CategoryDataOrchestrator
        self.logger.info("Getting final data...")

        category_data = category_orchestrator.get_final_category_data()
        # faculty_data = self.category_orchestrator.get_final_faculty_data()
        article_data = category_orchestrator.get_final_article_data()
        global_faculty_data = category_orchestrator.get_final_global_faculty_data()

        self.logger.info("Attempting to save data to database...")
        try:
            self.db.run_all_process(
                category_data=category_data,
                article_data=article_data,
                faculty_data=global_faculty_data,
            )
            self.logger.info(
                f"""Successfully saved to database!
                Categories: {len(category_data)}
                Articles: {len(article_data)}
                Faculty: {len(global_faculty_data)}
                """
            )
        except Exception as e:
            self.logger.error(f"Error saving to database: {e}")

    def _create_taxonomy(self) -> Taxonomy:
        return Taxonomy()

    def _create_classifier_factory(self) -> ClassifierFactory:
        return ClassifierFactory(
            taxonomy=self.taxonomy,
            ai_api_key=self.ai_api_key,
        )

    def _create_warning_manager(self) -> WarningManager:
        return WarningManager()

    def _create_strategy_factory(self) -> StrategyFactory:
        return StrategyFactory()

    def _create_utilities_instance(self) -> Utilities:
        return Utilities(
            strategy_factory=self.strategy_factory,
            warning_manager=self.warning_manager,
        )

    def _create_classification_orchestrator(self) -> ClassificationOrchestrator:
        return ClassificationOrchestrator(
            abstract_classifier_factory=self._get_acf_func(),
            utilities=self.utilities,
        )

    def _create_orchestrator(
        self, data: list[dict], extend: bool
    ) -> CategoryDataOrchestrator:
        return CategoryDataOrchestrator(
            data=data,
            output_dir_path=OUTPUT_FILES_DIR_PATH,
            category_processor=self.category_processor,
            faculty_postprocessor=self.faculty_postprocessor,
            warning_manager=self.warning_manager,
            strategy_factory=self.strategy_factory,
            utilities=self.utilities,
            dataclass_factory=self.dataclass_factory,
            extend=extend,
        )

    def _get_acf_func(self) -> Callable[[Dict[str, str]], ClassifierFactory]:
        """
        Returns a function that takes a dictionary of DOIs and abstracts and returns an AbstractClassifier.

        acf_func = abstract_classifier_factory function
        """
        return self._create_classifier_factory().abstract_classifier_factory

    def _validate_api_key(self, validator: APIKeyValidator, api_key: str) -> None:
        if not validator.is_valid(api_key=api_key):
            raise ValueError(
                "Invalid API key. Please check your API key and try again."
            )

    def _make_files(self) -> None:
        if not os.listdir(INPUT_FILES_DIR_PATH):
            raise Exception(
                f"Input directory: {INPUT_FILES_DIR_PATH} contains no files to process."
            )

        files_to_split = [
            os.path.join(INPUT_FILES_DIR_PATH, file)
            for file in os.listdir(INPUT_FILES_DIR_PATH)
            if file.endswith(".json")
        ]

        for file_path in files_to_split:
            self.utilities.make_files(
                path_to_file=file_path,
                split_files_dir_path=SPLIT_FILES_DIR_PATH,
            )

        return self

    def _load_files(self) -> list[dict]:
        """Load all split files into a list of dictionaries."""
        data_list: list[dict] = []
        for file_name in os.listdir(SPLIT_FILES_DIR_PATH):
            file_path = os.path.join(SPLIT_FILES_DIR_PATH, file_name)
            if not os.path.isfile(file_path):
                continue

            try:
                with open(file_path, "r") as file:
                    data = json.load(file)
                    data_list.append(data)
            except Exception as e:
                self.warning_manager.log_warning(
                    "File Loading", f"Error loading file: {file_path}. Error: {e}"
                )

        return data_list

    def _create_dataclass_factory(self) -> DataClassFactory:
        return DataClassFactory()

    def _create_crossref_wrapper(self, **kwargs) -> CrossrefWrapper:
        if "scraper" not in kwargs:
            kwargs["scraper"] = self.scraper if self.scraper else self._create_scraper()
        return CrossrefWrapper(**kwargs)

    def _create_category_processor(self) -> CategoryProcessor:
        return CategoryProcessor(
            utils=self.utilities,
            dataclass_factory=self.dataclass_factory,
            warning_manager=self.warning_manager,
            taxonomy_util=self.taxonomy,
        )

    def _create_faculty_postprocessor(self) -> FacultyPostprocessor:
        return FacultyPostprocessor()

    def _create_scraper(self) -> Scraper:
        return Scraper(api_key=self.ai_api_key)

    def _create_db(self) -> DatabaseWrapper:
        return DatabaseWrapper(db_name=self.db_name, mongo_url=self.mongodb_url)


if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()
    ai_api_key = os.getenv("OPENAI_API_KEY")
    mongodb_url = os.getenv("MONGODB_URL")
    pipeline_runner = PipelineRunner(
        ai_api_key=ai_api_key,
        crossref_affiliation="Salisbury%20University",
        data_from_year=2024,
        data_to_year=2024,
        mongodb_url=mongodb_url,
        debug=True,
    )
    pipeline_runner.run_pipeline()
