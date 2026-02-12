PJM Electricity Load Forecasting

---

# 1. Background

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

# 2. Data

## Data Source

Dataset Name: PJM Hourly Energy Consumption  
Source: Kaggle (Public Domain – CC0 License)  
Original Source: PJM Interconnection website  

File Used:
- PJME_hourly.csv
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

### Column 1: Datetime
- Data Type: Datetime (converted from string)
- Definition: Timestamp representing a specific hour
- Frequency: Hourly
- Example: 2004-12-31 23:00:00

---

### Column 2: PJME_MW
- Data Type: Integer / Float
- Definition: Electricity load in megawatts for that hour
- Potential Values: Continuous numeric values (e.g., 10000 – 60000 MW range)

---

## Target Variable (Label)

The target variable for the ML model will be:

PJME_MW (Hourly electricity load)

This is what we want to predict.

---

## Features (Predictor Variables)

From the Datetime column, the following features will be engineered:

- Hour of day (0–23)
- Day of week (0–6)
- Month
- Year
- Is weekend (binary)
- Seasonal indicators

These time-based features will serve as predictors in forecasting models.

---

## Modeling Approach

The project will explore:

- Baseline regression models
- Time-series forecasting approaches
- Performance evaluation using:
  - RMSE
  - MAE
  - Visual comparison of predicted vs actual load
