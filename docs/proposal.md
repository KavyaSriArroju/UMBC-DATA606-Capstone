# 1. Title and Author

**Project Title:** PJM Electricity Load Forecasting for Smart Grid Optimization  

**Author:** Kavya Sri Arroju  

**Semester:** Fall 2025  

**Prepared for:** UMBC Data Science Master Degree Capstone  
Dr. Chaojie (Jay) Wang  

**GitHub Repository Link:**  
https://github.com/KavyaSriArroju/UMBC-DATA606-Capstone

---


# 2. Background

## What is it about?
This study looks at more than a million hours of historical power usage in the PJM East area to forecast future hourly electrical consumption in this region of the country. The PJM Interconnection is one of the largest RTOs in North America, operating the electrical system for numerous states. 

Electricity usage changes greatly by hour of the day, day of the week and season due to weather, human activity and other economic factors. Accurate short-term load predictions are critical to maintaining a stable grid and effectively operating that grid (i.e. time between updates). 

This research analyzes over 10 years of historical hourly load data, identifies patterns and identifies predictive models for forecasting electricity loads in the future.

## Why does it matter?
Electric utilities must consistently and accurately balance the supply and demand for power among themselves.

A lack of accurate forecasting can cause:

Overproduction to occur, thus raising operating expenses
Instabilities in their grids and the potential for outages caused by underproduction
Inaccurate methods of purchasing energy
Inaccurate planning for demand-response strategies.

Accurate forecasting can assist:

To optimize means of reducing costs
To help manage peak loads
To facilitate the integration of renewable energy
To create successful bidding strategies within the energy business.

## Research Questions

This project aims to answer the following research questions:

1. What daily patterns exist in hourly electricity demand in the PJME region?
2. Are there strong weekly or seasonal trends in electricity consumption?
3. Which time-based features (hour of day, day of week, month) most influence electricity demand?
4. Can historical hourly load data be used to build an accurate short-term electricity load forecasting model?
5. How well can baseline regression or time-series models predict future electricity demand?


# 3. Data

## Data Source

Dataset Name: PJM Hourly Energy Consumption  
Source: Kaggle (Public Domain – CC0 License)  
Original Source: PJM Interconnection website 

Dataset Link:  
https://www.kaggle.com/datasets/robikscube/hourly-energy-consumption

File Used:  
PJME_hourly.csv

---

## Data Size

- File size: ~3–5 MB (depending on version)
- Total records: Approximately 140,000+ rows
- Columns: 2 columns (Datetime, PJME_MW)

---

## Time Period

The dataset covers approximately:
2002 to 2018 (over 10 years of hourly data)

---

## What Does Each Row Represent?

Each row represents:

One hour of electricity load (in Megawatts) in the PJM East region.

---

## Data Shape

Rows: ~140,000  
Columns: 2  

After feature engineering, additional columns will be created

## Data Dictionary

### Column Names, Data Types, Definitions, and Potential Values

| Column Name | Data Type | Definition | Potential Values |
|-------------|----------|------------|------------------|
| Datetime | Datetime | Timestamp representing one hour of electricity demand in the PJM East region | Hourly timestamps from 2002–2018 (e.g., 2015-07-01 13:00:00) |
| PJME_MW | Numeric (Float/Integer) | Electricity load measured in megawatts (MW) for that hour | Continuous numeric values (approximately 10,000 – 60,000 MW) |

---

### Target Variable (Label)

The target variable in the machine learning model will be:

**PJME_MW**

This represents the hourly electricity demand that the forecasting model aims to predict.

---

### Feature Variables (Predictors)

The following variables will be used as predictors in the forecasting model.  
These features will be engineered from the Datetime column:

| Feature Name | Data Type | Description | Potential Values |
|--------------|----------|------------|------------------|
| hour | Integer | Hour extracted from Datetime | 0 – 23 |
| dayofweek | Integer | Day of the week extracted from Datetime | 0 – 6 (0 = Monday, 6 = Sunday) |
| month | Integer | Month extracted from Datetime | 1 – 12 |
| year | Integer | Year extracted from Datetime | 2002 – 2018 |
| is_weekend | Binary | Indicator variable for weekend | 0 = Weekday, 1 = Weekend |

