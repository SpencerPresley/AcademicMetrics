![Header](./additional_information/images/am-header.png)

## Welcome to Academic Metrics

[![PyPi](https://img.shields.io/pypi/v/academic-metrics)](https://pypi.org/project/academic-metrics/) [![Documentation](https://img.shields.io/badge/docs-latest-blue)](https://academicmetrics.readthedocs.io/en/latest/) [![Example Site](https://img.shields.io/badge/example-site-green)](https://ai-taxonomy-front.vercel.app/)

[![GitHub issues](https://img.shields.io/github/issues/SpencerPresley/COSC425-DATA)](https://github.com/SpencerPresley/academic-metrics/issues) [![GitHub forks](https://img.shields.io/github/forks/SpencerPresley/COSC425-DATA)](https://github.com/SpencerPresley/academic-metrics/network) [![GitHub stars](https://img.shields.io/github/stars/SpencerPresley/COSC425-DATA)](https://github.com/SpencerPresley/academic-metrics/stargazers) [![GitHub license](https://img.shields.io/github/license/SpencerPresley/COSC425-DATA)](https://github.com/SpencerPresley/academic-metrics/blob/main/LICENSE) [![GitHub star chart](https://img.shields.io/github/stars/SpencerPresley/COSC425-DATA?style=social)](https://star-history.com/#SpencerPresley/COSC425-DATA) [![Downloads](https://static.pepy.tech/badge/academic-metrics/month)](https://pepy.tech/project/academic-metrics)

[![Share on Reddit](https://img.shields.io/badge/-Share%20on%20Reddit-orange)](https://www.reddit.com/submit?url=https%3A%2F%2Fgithub.com%2FSpencerPresley%2FCOSC425-DATA&title=Academic%20Metrics%20-%20AI-powered%20academic%20publication%20analysis) [![Share on X/Twitter](https://img.shields.io/badge/-Share%20on%20Twitter-blue)](https://twitter.com/intent/tweet?text=Check%20out%20Academic%20Metrics%20-%20AI-powered%20academic%20publication%20analysis%20%23AI%20%23Research%0A%0Ahttps%3A%2F%2Fgithub.com%2FSpencerPresley%2FCOSC425-DATA) [![Share on LinkedIn](https://img.shields.io/badge/-Share%20on%20LinkedIn-blue)](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fgithub.com%2FSpencerPresley%2FCOSC425-DATA&title=Academic%20Metrics%20-%20AI-powered%20academic%20publication%20analysis) [![Share on Hacker News](https://img.shields.io/badge/-Share%20on%20Hacker%20News-orange)](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fgithub.com%2FSpencerPresley%2FCOSC425-DATA&t=Academic%20Metrics%20-%20AI-powered%20academic%20publication%20analysis) [![Share on Pinterest](https://img.shields.io/badge/-Share%20on%20Pinterest-red)](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fgithub.com%2FSpencerPresley%2FCOSC425-DATA&description=Academic%20Metrics%20-%20AI-powered%20academic%20publication%20analysis) [![Share on Facebook](https://img.shields.io/badge/-Share%20on%20Facebook-blue)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fgithub.com%2FSpencerPresley%2FCOSC425-DATA) [![Share on Telegram](https://img.shields.io/badge/-Share%20on%20Telegram-blue)](https://telegram.me/share/url?url=https%3A%2F%2Fgithub.com%2FSpencerPresley%2FCOSC425-DATA&text=Academic%20Metrics%20-%20AI-powered%20academic%20publication%20analysis)

**What is Academic Metrics?**

*Academic Metrics* is an AI-powered toolkit for collecting, classifying, and analyzing academic publications.

The system can be used to:

- Collect publication data from Crossref API based on institutional affiliation
- Classify research into NSF PhD research focus areas utilizing LLMs
- Extract and analyze themes and methodologies from abstracts
- Generate comprehensive analytics at article, author, and category levels
- Store results in MongoDB (local or live via atlas), local JSON files, and Excel files

> [!TIP]
> Academic Metrics utilizes an early version of **[AIChainComposer](https://github.com/SpencerPresley/AIChainComposer)** for working with LLMs.
>
> **AIChainComposer** is a powerful tool to quickly, easily, and efficiently build out programmatic workflows with LLMs.
>
> **AIChainComposer** is now provided as a standalone package, and is available on [PyPI](pypi.org/project/ChainComposer/), allowing you to use the same tools that allowed for the development of Academic Metrics in your own projects.

## Table of Contents

- [Welcome to Academic Metrics](#welcome-to-academic-metrics)
- [Table of Contents](#table-of-contents)
- [Features](#features)
- [Documentation](#documentation)
- [Example Site and Demo](#example-site-and-demo)
- [Installation and Setup Steps](#installation-and-setup-steps)
  - [0. External Setup](#0-external-setup)
  - [1. Installation](#1-installation)
  - [2. Creating the directory and necessary files](#2-creating-the-directory-and-necessary-files)
  - [3. Virtual Environment (Optional but Recommended)](#3-virtual-environment-optional-but-recommended)
  - [4. Environment Variables](#4-environment-variables)
  - [5. Setting required environment variables](#5-setting-required-environment-variables)
    - [1. Open the `.env` file you just created, and add the following variables](#1-open-the-env-file-you-just-created-and-add-the-following-variables)
    - [2. Retrieve and set your MongoDB URI](#2-retrieve-and-set-your-mongodb-uri)
    - [3. Set your database name](#3-set-your-database-name)
    - [4. Set your OpenAI API Key](#4-set-your-openai-api-key)
  - [6. Using the package](#6-using-the-package)
    - [Option 1 (Short Script)](#option-1-short-script)
      - [1. Create the python file](#1-create-the-python-file)
      - [2. Copy paste the following code into the file you just created](#2-copy-paste-the-following-code-into-the-file-you-just-created)
      - [3. Run the script](#3-run-the-script)
    - [Option 2 (Command Line Interface)](#option-2-command-line-interface)
      - [1. Create the python file](#1-create-the-python-file-1)
      - [2. Copy and paste the following code into the file you just created](#2-copy-and-paste-the-following-code-into-the-file-you-just-created)
      - [3. Run the script](#3-run-the-script-1)
      - [Examples](#examples)
- [Wrapping Up](#wrapping-up)

## Features
****
| Category | Features | Benefits |
|----------|----------|-----------|
| 📊 Data Collection | • Crossref API Integration<br>• Smart Web Scraping<br>• Automated DOI Processing<br>• Multi-Source Data Fusion | • Comprehensive data gathering<br>• Enhanced data completeness<br>• Reliable source tracking<br>• Efficient data collection |
| 🤖 AI Classification | • LLM-Powered Analysis<br>• NSF PhD Focus Areas<br>• Theme Extraction<br>• Methodology Detection | • Accurate categorization<br>• Standardized classifications<br>• Insightful themes<br>• Research trend analysis |
| 📈 Analytics Engine | • Citation Tracking<br>• Author Statistics<br>• Department Analytics<br>• Category Analysis | • Impact measurement<br>• Performance tracking<br>• Department insights<br>• Research trends |
| 💾 Data Management | • MongoDB Integration<br>• JSON Export<br>• Excel Reports<br>• Flexible Storage | • Scalable storage<br>• Easy data sharing<br>• Familiar formats<br>• Data accessibility |
| 🔄 Processing Pipeline | • Async Processing<br>• Error Handling<br>• Rate Limiting<br>• Retry Logic | • Fast performance<br>• Reliable operation<br>• API compliance<br>• Robust processing |
| 🎯 Research Metrics | • Citation Impact<br>• Author Collaboration<br>• Research Focus<br>• Publication Trends | • Research evaluation<br>• Collaboration insights<br>• Focus area tracking<br>• Trend analysis |
| 🛠️ Developer Tools | • AIChainComposer Integration<br>• Modular Design<br>• Extensive Documentation<br>• CLI Interface | • Easy LLM integration<br>• Simple customization<br>• Quick learning<br>• Flexible usage |
| 🔍 Search & Discovery | • Full-Text Search<br>• Author Lookup<br>• Category Filtering<br>• Theme Analysis | • Easy exploration<br>• Quick lookups<br>• Focused results<br>• Theme discovery |
| 📱 Integration Ready | • Web API Support<br>• Example Site<br>• Data Export<br>• Custom Endpoints | • Easy deployment<br>• Quick visualization<br>• Data portability<br>• System integration |
| 🔐 Security & Control | • API Key Management<br>• Rate Control<br>• Error Logging<br>• Data Validation | • Secure operation<br>• Resource protection<br>• Better monitoring<br>• Data integrity |

## Documentation

To be able to see any and all implementation details regarding code logic, structure, prompts, and more you can check out our documentation. The documentation is built with [*Sphinx*](https://github.com/sphinx-doc/sphinx), allowing for easy use and a sense of famliarity.

[**Academic Metrics Documentation**](https://academicmetrics.readthedocs.io/en/latest/)

## Example Site and Demo

We also built an example site with the data we collected so that you can get a small idea of the potential uses for the data. This is by no means the only use case, but it does serve as a nice introduction to decide if this package would be useful for you.

> [!NOTE]
> The source code for the example site is available [here](https://github.com/cbarbes1/AITaxonomy-Front)

[**Example Site**](https://ai-taxonomy-front.vercel.app/)

> [!TIP]
> You can use our site source code for your own site!
> To easily launch your own website using the data you collect and classify via *Academic Metrics* see [**Site Creation Guide**](./additional_information/SiteCreationGuide.md)

To see a demo of the site, you can watch the below video:

[![Demo Video](https://img.youtube.com/vi/LojIwEvFgrk/maxresdefault.jpg)](https://youtu.be/LojIwEvFgrk)

---

## Installation and Setup Steps

Hey all, Spencer here, we are pleased to announce as of January 1st, 2025, you can now install the *Academic Metrics* package via *pip* and easily run the entire system via a short script or command line interface. Below are instructions outlining step by step how to do it. The steps walkthrough each piece of the process starting with installing python and setting up your environment, if you do not need help with those type of steps or want to jump straight to the code, first see [1. Installation](#1-installation), then you can skip to [6. Using the package](#6-using-the-package).

</br>

### 0. External Setup

1. **Installing and setting up Python 3.12:**

    While you should be able to use any version of Python >= 3.7, we recommend using Python 3.12 as that is the version we used to develop the system, and the one it's been tested on.

    For a detailed Python installation guide, see our [Python Installation Guide](./additional_information/_guides/_python_install.md).

2. **Installing and setting up MongoDB:**

    For a detailed MongoDB installation and setup guide, see our [MongoDB Installation Guide](./additional_information/_guides/_mongodb_install.md).

    Once you have MongoDB installed and running, you can create a database to store your data in, if you haven't already.

    To create a new database, you can run:

    ```bash
    use <db_name>
    ```

    If you need more help, the MongoDB Installation Guide goes into more detail on how to create a database and verify it exists.

    Collection creation is handled by the system, you do not need to create them.

    </br>

    ---

### 1. Installation

Install `academic_metrics>=1.0.98` via pip.

To install the latest version of the package, you can run the following command:

```bash
pip install academic-metrics
```

### 2. Creating the directory and necessary files

1. **Create the directory and navigate into it:**

   For this example we will be using `am_data_collection` as the name of the directory, but you can name it whatever you want.

    **All systems (seperate commands):**

    ```bash
    mkdir am_data_collection
    cd am_data_collection
    ```

    Or as a single line:

    **Linux / Mac / Windows Command Prompt**:

    ```bash
    mkdir am_data_collection && cd am_data_collection
    ```

    **Windows Powershell**:

    ```powershell
    mkdir am_data_collection; cd am_data_collection
    ```

</br>

### 3. Virtual Environment (Optional but Recommended)

Now that you've created and entered your project directory, you can set up a virtual environment.

For detailed instructions on setting up and using virtual environments, see our [Python Installation Guide - Virtual Environments Section](./additional_information/_guides/_python_install.md#setting-up-virtual-environments).

After setting up your virtual environment, return here to continue with the next steps.

</br>

### 4. Environment Variables

**Create a `.env` file inside the directory you just created.**

**Linux/Mac**:

```bash
touch .env
```

**Windows** (Command Prompt):

```cmd
type nul > .env
```

**Windows** (PowerShell):

```powershell
New-Item -Path .env -Type File
```

You should now have a `.env` file in your directory.

</br>

### 5. Setting required environment variables

</br>

#### 1. Open the `.env` file you just created, and add the following variables

- a variable to store your MongoDB URI, I recommend `MONGODB_URI`
- a variable to store your database name, I recommend `DB_NAME`
- a variable to store your OpenAI API Key, I recommend `OPENAI_API_KEY`

 After each variable you should add `=""` to the end of the variable.

 Once you've done this, your `.env` file should look something like this:

```python
MONGODB_URI=""
DB_NAME=""
OPENAI_API_KEY=""
```

</br>

#### 2. Retrieve and set your MongoDB URI

For local MongoDB it's typically:

```python
MONGODB_URI="mongodb://localhost:27017"
```

For live MongoDB:

For a live version you should use the MongoDB Atlas URI. It should look something like this:

```bash
mongodb+srv://<username>:<password>@<cluster-name>.<unique-id>.mongodb.net/?retryWrites=true&w=majority&appName=<YourAppNameOnAtlas>
```

So in the `.env` file you should have something that looks like this:

Local:

```python
MONGODB_URI="mongodb://localhost:27017"
```

Live:

```python
MONGODB_URI="mongodb+srv://<username>:<password>@<cluster-name>.<unique-id>.mongodb.net/?retryWrites=true&w=majority&appName=<YourAppNameOnAtlas>"
```

</br>

> [!WARNING]
> I recommend starting locally unless you need to use a live MongoDB instance.
> This will avoid the need to deal with setting up MongoDB Atlas, which while not difficult, it is an added step.

</br>

#### 3. Set your database name

You can pick any name you want for `DB_NAME`, but it needs to be a name of a valid database on your mongodb server. To make one on the command line you can run:

```bash
mongosh
use <db_name>
```

For this demonstration we will be using `academic_metrics_data` as the `DB_NAME`.

First we'll create the database on the command line:

```bash
mongosh
use academic_metrics_data
```

This is to ensure the database actually exists so that the system can access it.

Now that the database exists, we'll set the `DB_NAME` in the `.env` file.

```python
DB_NAME="academic_metrics_data"
```

</br>

#### 4. Set your OpenAI API Key

If you do not have an OpenAI API key you will need to create one, but do not worry, it's easy.

Go to the following link and click on "+ Create new secret key":

[https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)

Give the key a name, and then copy the key.

Then in the `.env` file paste the key in the `OPENAI_API_KEY` variable.

It should look similar to this, but with the full key instead of `sk-proj...`:

```python
OPENAI_API_KEY="sk-proj..."
```

</br>

> [!IMPORTANT]
> You will need to add funds to your OpenAI account to use the API.
>
> When using the default model for the system (gpt-4o-mini), it cost us about $3-4 dollars to process all of the data from Salisbury University from 2009-2024.
>
> For larger models such as gpt-4o, the cost will be much higher.
>
> We saw good results using gpt-4o-mini, and it's also the most cost effective. So I recommend starting with that.
>
> Additionally, whether you opt to use our command line interface or your own script, the data is processed one month at a time and saved to the database, so if you run out of funds on your OpenAI account you will not lose data for the entire run, only the current month being processed. Simply add funds to your account and continue.
>
> You do not have to change anything in the code once you run it again, the system checks for existing data and only processes data that has not yet been processed.

</br>

All together your `.env` file should look like this:

```python
MONGODB_URI="mongodb://localhost:27017"
DB_NAME="academic_metrics_data"
OPENAI_API_KEY="sk-proj..."
```

</br>

### 6. Using the package

To use the system, you have 2 options:

1. Writing a short script (code provided) to loop over a range of dates you'd like to collect.

2. Using a provided function to run a command line interface version.

For most users, I recommend the second option, it's only a few lines of code which you can copy and paste, the rest of the usage is handled by the command line interface and doesn't require any additional coding, you can find the second option in the [Option 2 (Command Line Interface)](#option-2-command-line-interface) section.

On the other hand, if you plan on using the main system, or other tools within the package within your own scripts, or just don't enjoy using command line interfaces, I recommend the first option.

While I recommend the second option unless you're planning on using the package's offerings in a more complex manner, the basic code to run the system for the first option is provided in full in [Option 1 (Short Script)](#option-1-short-script) section.

To see some examples of more complex use cases with examples, you can check out the [Other Uses](./additional_information/OtherUses.md) section.

</br>

#### Option 1 (Short Script)

For this option you need to do the following:
</br>
</br>

##### 1. Create the python file

Within your directory, create a new python file, for this example we will be using `run_am.py`, but you can name it whatever you want.

**Linux/Mac**:

```bash
touch run_am.py
```

**Windows (Command Prompt):**

```cmd
type nul > run_am.py
```

**Windows (PowerShell):**

```powershell
New-Item -Path run_am.py -Type File
```

You should now have a python file in your directory whose name matches the one you created.

</br>

##### 2. Copy paste the following code into the file you just created

```python

# dotenv is the python package responsible for handling env files
from dotenv import load_dotenv

# os is used to get the environment variables from the .env file
import os

# PipelineRunner is the main class used to run the pipeline
from academic_metrics.runners import PipelineRunner

# load_dotenv is used to load the environment variables from the .env file
load_dotenv()

# Get the environment variables from the .env file
ai_api_key = os.getenv("OPENAI_API_KEY")
mongodb_uri = os.getenv("MONGODB_URI")
db_name = os.getenv("DB_NAME")

# Set the date range you want to process
# Years is a list of years as strings you want to process
# Months is a list of strings representing the months you want processed for each year
# For example if you want to process data from 2009-2024 for all months out of the year, you would do:
# Note: the process runs left to right, so from beginning of list to the end of the list,
# so this will process 2024, then 2023, then 2022, etc.
# Data will be saved after each month is processed.
years = [
    "2024",
    "2023",
    "2022",
    "2021",
    "2020",
    "2019",
    "2018",
    "2017",
    "2016",
    "2015",
    "2014",
    "2013",
    "2012",
    "2011",
    "2010",
    "2009",
]
months = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

# Loop over the years and months and run the pipeline for each month
# New objects are created for each month to avoid memory issues as well as to avoid overwriting data
for year in years:
    for month in months:

        # Create a new PipelineRunner object for each month
        # parameters:
        # ai_api_key: the OpenAI API key
        # crossref_affiliation: the affiliation to use for the Crossref API
        # data_from_month: the month to start collecting data from
        # data_to_month: the month to end collecting data on
        # data_from_year: the year to start collecting data from
        # data_to_year: the year to end collecting data on
        # mongodb_uri: the URL of the MongoDB server
        # db_name: the name of the database to use
        pipeline_runner = PipelineRunner(
            ai_api_key=ai_api_key,
            crossref_affiliation="Salisbury University",
            data_from_month=int(month),
            data_to_month=int(month),
            data_from_year=int(year),
            data_to_year=int(year),
            mongodb_uri=mongodb_uri,
            db_name=db_name,
        ) 

        # Run the pipeline for the current month
        pipeline_runner.run_pipeline()
```

If you'd like to save the data to excel files in addition to the other data formats, you can do so via importing the function `get_excel_report` from `academic_metrics.runners` and calling it at the end of the script.

Full code for convenience:

```python

# dotenv is the python package responsible for handling env files
from dotenv import load_dotenv

# os is used to get the environment variables from the .env file
import os

# PipelineRunner is the main class used to run the pipeline
# get_excel_report is the function used to save the data to excel files
# it takes in a DatabaseWrapper object as a parameter, which connects to the database
# and retrives the data before writing it to 3 seperate excel files. One for each data type.
from academic_metrics.runners import PipelineRunner, get_excel_report

# DatabaseWrapper is the class used to connect to the database and retrieve the data
from academic_metrics.DB import DatabaseWrapper

# load_dotenv is used to load the environment variables from the .env file
load_dotenv()

# Get the environment variables from the .env file
# If you used the same names as the ones in the examples, you can just copy paste these
# if you used different names, you will need to change them to match the ones in your .env file
ai_api_key = os.getenv("OPENAI_API_KEY")
mongodb_uri = os.getenv("MONGODB_URI")
db_name = os.getenv("DB_NAME")

# Set the date range you want to process
# Years is a list of years as strings you want to process
# Months is a list of strings representing the months you want processed for each year
# For example if you want to process data from 2009-2024 for all months out of the year, you would do:
# Note: the process runs left to right, so from beginning of list to the end of the list,
# so this will process 2024, then 2023, then 2022, etc.
# Data will be saved after each month is processed.
years = [
    "2024",
    "2023",
    "2022",
    "2021",
    "2020",
    "2019",
    "2018",
    "2017",
    "2016",
    "2015",
    "2014",
    "2013",
    "2012",
    "2011",
    "2010",
    "2009",
]
months = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

# Loop over the years and months and run the pipeline for each month
#
# New objects are created for each month 
# to avoid memory issues as well as to avoid overwriting data
for year in years:
    for month in months:

        # Create a new PipelineRunner object for each month
        # parameters:
        # ai_api_key: the OpenAI API key
        # crossref_affiliation: the affiliation to use for the Crossref API
        # data_from_month: the month to start collecting data from
        # data_to_month: the month to end collecting data on
        # data_from_year: the year to start collecting data from
        # data_to_year: the year to end collecting data on
        # mongodb_uri: the URL of the MongoDB server
        # db_name: the name of the database to use
        pipeline_runner = PipelineRunner(
            ai_api_key=ai_api_key,
            crossref_affiliation="Salisbury University",
            data_from_month=int(month),
            data_to_month=int(month),
            data_from_year=int(year),
            data_to_year=int(year),
            mongodb_uri=mongodb_uri,
            db_name=db_name,
        ) 

        # Run the pipeline for the current month
        pipeline_runner.run_pipeline()

# Create a new DatabaseWrapper object so it can be given to get_excel_report
db = DatabaseWrapper(db_name=db_name, mongo_uri=mongodb_uri)

# Call the get_excel_report function, passing in the db object, to save the data to excel files
#
# Once this finishes running, you should have 3 excel files in your directory:
# article_data.xlsx, faculty_data.xlsx, and category_data.xlsx
get_excel_report(db)
```

</br>

##### 3. Run the script

```bash
python run_am.py
```

</br>

#### Option 2 (Command Line Interface)

For this options you will still need to create a python file, but the code will only be a couple lines long as you'll be passing in your arguments via the command line.

</br>

##### 1. Create the python file

Within your directory, create a new python file, for this example we will be using `run_am.py`, but you can name it whatever you want.

**Linux/Mac**:

```bash
touch run_am.py
```

**Windows (Command Prompt):**

```cmd
type nul > run_am.py
```

**Windows (PowerShell):**

```powershell
New-Item -Path run_am.py -Type File
```

You should now have a python file in your directory whose name matches the one you created.

</br>

##### 2. Copy and paste the following code into the file you just created

```python
from dotenv import load_dotenv
from academic_metrics.runners import command_line_runner

load_dotenv()

command_line_runner()
```

> [!WARNING]
> If you did not use `MONGODB_URI` and `OPENAI_API_KEY` as the variable names in the .env file, you will need to make a couple changes to the above code.

**How to use with different variable names:**

The `command_line_runner` function takes in 2 optional arguments:

- `openai_api_key_env_var_name`
- `mongodb_uri_env_var_name`

Which correspond to the names of the environment variables you used in your .env file.

To use the different names, do the following:

```python
from dotenv import load_dotenv
from academic_metrics.runners import command_line_runner

load_dotenv()

# The strings should be changes to match the names you used in your .env file
command_line_runner(
    openai_api_key_env_var_name="YOUR_OPENAI_API_KEY_ENV_VAR_NAME",
    mongodb_uri_env_var_name="YOUR_MONGODB_URI_ENV_VAR_NAME",
)
```

</br>

##### 3. Run the script

For this option you will still run the script from command line, but you will also be passing in arguments, details laid out below.

There are various command line arguments you can pass in, almost all are detailed here, but to see a complete list you can run:

```bash
python run_am.py --help
```

When running the script, you can configure the pipeline by passing in the following arguments:

- `--from-month` - The month to start collecting data from, defaults to 1
- `--to-month` - The month to end collecting data on, defaults to 12
- `--from-year` - The year to start collecting data from, defaults to 2024
- `--to-year` - The year to end collecting data on, defaults to 2024
- `--db-name` - The name of the database to use (required)
- `--crossref-affiliation` - The affiliation to use for the Crossref API, defaults to Salisbury University (required)

If you want to save the data to excel files you can pass in the `--as-excel` argument.

>[!NOTE]
> The `--as-excel` argument is an additional action, it doesn't remove the the saving to other data formats, but merely adds the excel saving functionality.

</br>

##### Examples

Say you want to collect data for every month from 2019 to 2024 for Salisbury University and save it to excel files. You would run the following command:

```bash
python run_am.py --from-month=1 \
--to-month=12 \
--from-year=2019 \
--to-year=2024 \
--crossref-affiliation="Salisbury University" \
--as-excel \
--db-name="Your_Database_Name"
```

To make this simpler, we can actually take advantage of the default values for some of the arguments.

Recall from before:

- `--from-month` defaults to `1`
- `--to-month` defaults to `12`
- `--from-year` defaults to `2024`
- `--to-year` defaults to `2024`
- `--crossref-affiliation` defaults to `Salisbury University`

Using the defaults, we can make that command much more concise:

```bash
python run_am.py \
--from-year=2019 \
--as-excel \
--db-name="Your_Database_Name"
```

</br>

**On AI Models**:

The default AI (LLM) model used for all phases is `gpt-4o-mini`. You can specify a different model for each phase independently by passing in the following arguments:

- `--pre-classification-model` - The model to use for the pre-classification step
- `--classification-model` - The model to use for the classification step
- `--theme-model` - The model to use for the theme extraction step

Here's how you would run the pipeline using the larger `gpt-4o` model:

```bash
python run_am.py --from-month=1 \
--to-month=12 \
--from-year=2019 \
--to-year=2024 \
--crossref-affiliation="Salisbury University" \
--as-excel \
--db-name="Your_Database_Name" \
--pre-classification-model="gpt-4o" \
--classification-model="gpt-4o" \
--theme-model="gpt-4o"
```

and taking advantage of the defaults:

```bash
python run_am.py \
--from-year=2019 \
--as-excel \
--db-name="Your_Database_Name" \
--pre-classification-model="gpt-4o" \
--classification-model="gpt-4o" \
--theme-model="gpt-4o"
```

>[!WARNING]
> This process consumes a lot of tokens, and OpenAI API service usage is based off the number of input/output tokens used, with each model having different cost per input/output token.
>
> You can check the cost of each model at [https://openai.com/api/pricing/](https://openai.com/api/pricing/).
>
> During testing we found that using `gpt-4o-mini` was the most cost effective.
>
> In addition we spent a lot of time testing prompts and models, our prompts have been tuned to a point where they elicit good results from `gpt-4o-mini`, thus a larger model may not be necessary to get the results you want.
>
> If you want to use a larger model like `gpt-4o`, whether it be out of curiosity or you want to see if it provides better results, I still recommend you start with a smaller date range to get an idea of what it will cost. If you find the cost to be acceptable, then you can start expanding the date range.

</br>

**Other institutions**:

Our system uses the Crossref API to collect available data, then it scrapes the DOI link to get any missing data as well as any additional data that may be available.

We found that the Crossref API sometimes misses some Abstracts for example, our scraping process will fill in nearly all, if not all, of the missing abstracts.

Due to this, and the wealth of institutions Crossref covers, you can use the system for any institution that has a DOI link.

Here's how you'd run the same query on the system but for **University of Maryland** data:

```bash
python run_am.py \
--from-year=2019 \
--as-excel \
--db-name="Your_Database_Name" \
--crossref-affiliation="University of Maryland"
```

You can even go back as far as you want, for example say you want to collect all data from the beginning of the 21st century:

```bash
python run_am.py \
--from-year=2000 \
--as-excel \
--db-name="Your_Database_Name" \
--crossref-affiliation="University of Maryland"
```

Or maybe you want to collect all data as far back as possible, so you can see longterm trends and history of the institution:

```bash
python run_am.py \
--from-year=1900 \
--as-excel \
--db-name="Your_Database_Name" \
--crossref-affiliation="University of Maryland"
```

The from year does not require that there be data that far back, it simply means that is the cutoff point for the data you want to collect.

So say you're not entirely sure what year your University started, or aren't sure how far back Crossref covers, you can simply enter a very far back year, like 1900, and the system will collect all data from that year and onwards.

---

## Wrapping Up

That's it! You've now successfully installed and run the system.

If you have any questions, need help, or have interest in collaborating on this project or others, feel free to reach out to me, contact information is provided below.

If you are a potential employer, please reach out to me by email or linkedin, contact information is provided below.

Contact information:

- Email: [spencerpresley96@gmail.com](mailto:spencerpresley96@gmail.com)
- LinkedIn: [https://www.linkedin.com/in/spencerpresley96/](https://www.linkedin.com/in/spencerpresley96/)

Happy coding!
