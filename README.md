# Unveiling the World of Formula 1 Through Numbers [Project in progress]

This project is a result of my passion for data analysis and fascination with the world of Formula 1 and is still being developed. For now only some aspects of this prestigious sport are encompassed - race results, driver data and teams. Dataset comes from Kaggle platform - https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020.

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


## Project Goals:

The objective of this project was to conduct a comprehensive analysis of Formula 1 data to identify trends, patterns, and intriguing insights related to the history of this sport. It also aimed to utilize Python programming skills and data analysis tools to create a comprehensive visual and cognitive analysis.

## Project Phases:

### 1. Driver and Team Analysis: I focused on analyzing the achievements of drivers and teams to identify dominant figures and brands in different periods.


#### 1. Driver age analysis

1.1. Analyzing the age of drivers at the time of debut and at 
the time of first win in Grand Prix.

1.2. Analyzing the average age of drivers in various periods 
between 1950 and 2023.


#### 2. Drivers from different countries

2.1. Analyzing the achievements of drivers from different countries.

2.2. Identifying the dominant nationalities in Formula 1.

#### 3. Analysis of driver's careers

3.1. Analyzing the length of driver's careers in Formula 1.

3.2. Identification of drivers who have spent their entire 
career with one team.

#### 4. Multiple champion drivers

4.1. Analysis of drivers who have won the Formula 1 championship 
more than once.

#### 5. Team changes

5.1. The impact of changing teams on driver's mean points 
results per race.


### 3. Data Visualization: I created some data visualizations that aided in a better understanding of the presented information.
