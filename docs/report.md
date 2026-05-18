# PJM Electricity Load Forecasting using Machine Learning

**Kavya Sri Arroju**  
**DATA 606 Capstone Project – Spring 2026**

---

## Project Links

- **GitHub Repository:**  
  https://github.com/KavyaSriArroju/UMBC-DATA606-Capstone/tree/main

- **Presentation Video (YouTube):**  
[https://www.youtube.com/watch?v=hBpBQHxgnKY]
- **Final PPT Presentation:**  
  [https://github.com/KavyaSriArroju/UMBC-DATA606-Capstone/blob/main/docs/Capstone_Presentation.pptx]

---

# Background

Electricity demand forecasting is an important problem in energy management and smart grid systems. Power companies need accurate predictions of electricity consumption in order to balance electricity generation and demand efficiently. Incorrect predictions may lead to higher operational costs, energy wastage, or even power outages.

Electricity usage changes continuously throughout the day depending on human activities, weather conditions, seasonal effects, and industrial operations. Because of these changing patterns, forecasting electricity demand becomes a complex time-series prediction problem.

The goal of this project is to use machine learning techniques to predict hourly electricity demand using historical electricity load data from the PJM Interconnection region in the United States. In addition to prediction modeling, an interactive Streamlit dashboard was developed for visualization and monitoring of electricity demand patterns and prediction results.

---

# Data Sources

The dataset used in this project is the **PJM Hourly Energy Consumption Dataset** obtained from Kaggle.

Dataset Source:  
https://www.kaggle.com/datasets/robikscube/hourly-energy-consumption

The dataset contains hourly electricity load data collected from the PJM Interconnection power grid region. The data spans from approximately 2002 to 2018 and contains around 145,000 observations.

The original dataset file used in this project is:

```text
PJME_hourly.csv
```

The processed feature-engineered dataset was also created for modeling purposes.
---

# Data Elements

The target variable used in this project is:

| Variable | Description |
|---|---|
| PJME_MW | Hourly electricity demand measured in megawatts |

Several additional features were created during feature engineering to improve model performance.

## Time-Based Features

- Hour
- Day of week
- Month
- Year
- Weekend indicator

## Lag Features

- lag_1
- lag_24
- lag_168

## Rolling Features

- rolling_mean_24
- rolling_std_24

## Cyclical Encoding Features

- hour_sin
- hour_cos
- month_sin
- month_cos

These engineered features helped the machine learning models better understand repeating time-series patterns.

---

# Exploratory Data Analysis (EDA)

Exploratory data analysis was performed to understand electricity demand behavior and identify trends and patterns in the dataset.

Several visualizations were created to analyze hourly, daily, weekly, and monthly electricity demand patterns.

## Key Findings from EDA

### Hourly Trends

Electricity demand generally increases during daytime and evening hours and decreases late at night.

### Weekly Patterns

Electricity usage tends to be higher during weekdays compared to weekends.

### Seasonal Patterns

Demand varies across months and seasons because of weather and human activities.

### Time-Series Behavior

The dataset shows strong repeating patterns and cyclical trends suitable for time-series forecasting.

---

# Feature Engineering

Feature engineering was one of the most important steps in this project.

Several new features were created from the datetime column to improve prediction accuracy.

Time-based features such as hour, day, month, and year were extracted from the timestamp.

Lag features were created using previous electricity demand values to capture historical trends.

Rolling averages and rolling standard deviation features were also added to smooth fluctuations.

These engineered features significantly improved model performance.

---

# Machine Learning Models

Two machine learning models were implemented and compared in this project.

## Linear Regression

Linear Regression was used as the baseline model because it is simple and interpretable.

## Random Forest Regressor

Random Forest was used as the advanced model because it captures complex and non-linear relationships effectively.

The dataset was split into training and testing sets using a time-based split approach.

---

# Model Evaluation

The following evaluation metrics were used to compare model performance:

| Metric | Description |
|---|---|
| MAE | Mean Absolute Error |
| RMSE | Root Mean Square Error |
| R² | Coefficient of Determination |

## Model Comparison Results

| Model | MAE | RMSE | R² |
|---|---|---|---|
| Linear Regression | 777.97 | 994.14 | 0.9765 |
| Random Forest | 286.93 | 396.38 | 0.9963 |

The Random Forest model achieved significantly better performance compared to Linear Regression.

---

# Actual vs Predicted Results

An actual versus predicted graph was generated to compare real electricity demand values with model predictions.

The predicted values closely followed the actual electricity demand trends and fluctuations, showing strong model accuracy.

---

# Streamlit Dashboard

An interactive dashboard was developed using Streamlit to make the project more practical and user-friendly.

The dashboard allows users to:

- Upload the processed dataset
- Visualize electricity demand trends
- Compare model performance
- View prediction graphs
- Monitor electricity demand status

The dashboard also includes a demand status indicator that classifies electricity usage as low, normal, high, or critical.

This interactive component improves the usability and presentation of the project.

---

# Conclusion

This project successfully demonstrated the use of machine learning for electricity load forecasting.

Exploratory data analysis revealed strong temporal and seasonal patterns in electricity demand.

Feature engineering significantly improved prediction accuracy.

Among the models tested, Random Forest achieved the best performance because it effectively captured complex and non-linear relationships.

The project also included an interactive Streamlit dashboard for visualization and monitoring purposes.

---

# Limitations

Although the project achieved strong prediction performance, several limitations exist.

- Weather data was not included
- Holiday information was not incorporated
- Only two models were compared
- Real-time API integration was not implemented

These limitations provide opportunities for future improvements.

---

# Future Research Directions

Several improvements can be explored in future work.

- Add weather-related features
- Include holiday and event information
- Explore deep learning models such as LSTM
- Integrate real-time electricity demand APIs
- Deploy the dashboard online for public access

These improvements can help build a more advanced and production-ready forecasting system.

---

# References

1. Kaggle – PJM Hourly Energy Consumption Dataset  
https://www.kaggle.com/datasets/robikscube/hourly-energy-consumption

2. Scikit-learn Documentation  
https://scikit-learn.org/

3. Streamlit Documentation  
https://docs.streamlit.io/

4. Pandas Documentation  
https://pandas.pydata.org/

5. Matplotlib Documentation  
https://matplotlib.org/
