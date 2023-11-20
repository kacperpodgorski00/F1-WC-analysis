![cars](https://github.com/kacperpodgorski00/F1-WC-analysis/assets/73601611/b2cdcd17-42ed-454e-b01d-4e4ac310e89c)

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

![1 1](https://github.com/kacperpodgorski00/F1-WC-analysis/assets/73601611/d73ebe9e-377b-4bad-90f2-8236e1572ec8)

![1 1_scatt](https://github.com/kacperpodgorski00/F1-WC-analysis/assets/73601611/2699edf1-ca7e-484b-8f0b-7ad0b7038058)

![1 1_kde](https://github.com/kacperpodgorski00/F1-WC-analysis/assets/73601611/6739801c-82a5-4673-a339-a503f4f62dca)

1.2. Analyzing the average age of drivers in various periods 
between 1950 and 2023.

![1 2](https://github.com/kacperpodgorski00/F1-WC-analysis/assets/73601611/ff9a53ae-9463-4e27-aa15-aceea397975a)

![1 2_bar](https://github.com/kacperpodgorski00/F1-WC-analysis/assets/73601611/dcf05340-b5f3-41ae-a656-d63dae39b4c5)

#### 2. Drivers from different countries

2.1. Analyzing the achievements of drivers from different countries.

![2 1](https://github.com/kacperpodgorski00/F1-WC-analysis/assets/73601611/aad1fb27-4a37-45b0-9d53-d0cbfa3c494c)

![2 1_bar](https://github.com/kacperpodgorski00/F1-WC-analysis/assets/73601611/f673a483-bca2-4593-a235-83639a4865c4)

![2 1_bar2](https://github.com/kacperpodgorski00/F1-WC-analysis/assets/73601611/ee470bb1-7e64-4863-a799-cf15b4c4c741)

#### 3. Analysis of driver's careers

3.1. Analyzing the length of driver's careers in Formula 1.

![3 1](https://github.com/kacperpodgorski00/F1-WC-analysis/assets/73601611/56389ada-1ecf-4adb-ac3a-faaf3e246fb3)

![3 1_bar](https://github.com/kacperpodgorski00/F1-WC-analysis/assets/73601611/427fef9f-9ae5-495d-b859-017be774bee8)

3.2. Identification of drivers who have spent their entire 
career with one team.

![3 2](https://github.com/kacperpodgorski00/F1-WC-analysis/assets/73601611/862bcc2f-679c-481b-86a6-126f16871af5)

#### 4. Multiple champion drivers

4.1. Analysis of drivers who have won the Formula 1 championship 
more than once.

![4 1](https://github.com/kacperpodgorski00/F1-WC-analysis/assets/73601611/e4372996-a8db-4338-805c-12961836bc2b)

#### 5. Team changes

5.1. The impact of changing teams on driver's mean points 
results per race.

![5 1](https://github.com/kacperpodgorski00/F1-WC-analysis/assets/73601611/fed7c284-b284-41e1-a7a8-b71ee9ce42fb)


