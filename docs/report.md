# 1. Title and Author

- **Project Title** – PJM Electricity Load Forecasting using Machine Learning  
- **Author** – Kavya Sri Arroju  
- **Semester** – Spring '26  
- **Prepared for** – UMBC Data Science Master Degree Capstone
- **Instructor** – Dr. Chaojie Wang

---

## Project Links

- **GitHub Repository:**  
  https://github.com/KavyaSriArroju/UMBC-DATA606-Capstone/tree/main

- **Presentation Video (YouTube):**  
[https://www.youtube.com/watch?v=hBpBQHxgnKY]
- **Final PPT Presentation:**  
  [https://github.com/KavyaSriArroju/UMBC-DATA606-Capstone/blob/main/docs/Capstone_Presentation.pptx]

---

# 2. Background

Forecasting electricity demand is a crucial issue in energy management and smart grid systems. Power companies are required to have accurate forecasts of electricity consumption to be able to efficiently balance the generation and demand for electricity. Inaccurate forecasts may result in increased operational costs, waste of energy, and the potential for interruptions in service.

Electricity demand is continuously changing during the day due to human activities, weather conditions, a variety of seasonal effects, and industrial processes. Therefore, due to these changing patterns, predicting electricity demand becomes a complex forecasting problem that can be treated as a time-series prediction problem.

The purpose of this project is to predict hourly electricity demand by using machine learning approaches to analyze historical electricity load data from the PJM Interconnection region of the U.S. Another product of this project is a Streamlit dashboard for users to visualize electricity demand patterns and make real-time predictions.
---

# 3. Data Sources

The data used in this project is the PJM Hourly Energy Consumption Dataset from Kaggle. 

Dataset Source:  
https://www.kaggle.com/datasets/robikscube/hourly-energy-consumption

This hourly energy consumption dataset reports on the hourly energy consumption data (electricity load) from the PJM Interconnection region of the U.S. The hourly energy consumption dataset consists of approximately 145,000 observations that cover roughly from 2002 to 2018.

The original dataset file used in this project is:

```text
PJME_hourly.csv
```

A dataset featuring information engineered was outputted to be available for modeling.

---

# 4. Data Elements

The target variable used in this project is:

| Variable | Description |
|---|---|
| PJME_MW | Hourly electricity demand measured in megawatts |

During the process of feature engineering, additional features were generated with the intention of enhancing the effectiveness of the model.

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

By assisting the machine learning model in identifying repeating patterns of time-series, the engineered features ultimately improved machine learning model learning capability.

---

# 5. Exploratory Data Analysis (EDA)

In order to gain an understanding of electricity demand behaviour, exploratory data analysis was used and to assist with the identification of trends and patterns noted within the dataset.

A number of visualisations were produced for the purpose of analysing electricity demand patterns at an hourly, daily, weekly and monthly level.

## Key Findings from EDA

### Hourly Trends

Electricity demand will typically rise during daylight hours and evenings but will drop late evening.

### Weekly Patterns

Electricity will generally be consumed more on weekdays as opposed to weekends.

### Seasonal Patterns

Demand can vary throughout a month and seasonally due to both climatic and human conversion reasons.

### Time-Series Behavior

The provided dataset contained evidence of strong repeating and cyclic trends that were typical for time-series forecasting.

---

# 6. Feature Engineering

The feature engineering performed was one of the most critical components of the entire project.

The date/time column produced a number of new features used to produce more accurate predictions.

The date/time column contained extracted time based features i.e., hour, day, month, year.

Time lagged features were created using the previous period of electricity demand to capture historical trends versus current trends.

Rolling averages and rolling standard deviations were also added to smooth fluctuating demand levels.

These engineered features greatly enhanced the effectiveness of the models.

---

# 7. Machine Learning Models

In this project, two machine learning models were evaluated and compared against one another.

## Linear Regression

The baseline model that was selected is called Linear Regression; this type of model is relatively simple and therefore easy to interpret and explain.

## Random Forest Regressor

The second model that was selected was Random Forest. This particular Machine Learning modeling approach has been shown to be extremely effective at modeling complex and non-linear relationships.

To evaluate and compare the two models, the dataset was split into two sets using a "time-based" split approach; thus, one set of data was used to build each model while the second set was used to test the performance of each model.

---

# 8. Model Evaluation

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

The results, when comparing model performance, indicated that the Random Forest Model outperformed the Linear Regression Model by a significant margin.

---

# 9. Actual vs Predicted Results

An "Actual vs. Predicted" graph was created to demonstrate the relationship between the actual values of electricity demand and those predicted by the model.

Comparing the predicted values to the actual electricity demand values indicated that there was a strong level of model performance, with the predicted values closely following the actual demand trends and fluctuations.

---

# 10. Streamlit Dashboard

Streamlit was utilized to create an interactive dashboard that added practical value to the project as well as created an easy-to-use and friendly experience for project users.

The dashboard allows users to:

- Upload the processed dataset
- Visualize electricity demand trends
- Compare model performance
- View prediction graphs
- Monitor electricity demand status

Finally, the interactive dashboard indicates the status of electricity usage, therefore classifying the electricity consumption as either Low, Normal, High or Critical.

This type of user interactivity not only enhances the usability of the project, but also dramatically improves the presentation of the project.

---

# 11. Conclusion

Machine learning was used effectively in this project to predict future electric demand. 

By analysing electric demand data, it was found that there are recurring seasonal and temporal trends.

The accuracy of the model predictions improved by feature engineering.

Random Forest produced the best results of all the models tested, because it was successful in detecting more complicated and nonlinear patterns in the data.

An interactive dashboard created using Streamlit was also developed as a means for monitoring and visualising electric usage.

---

# 12. Limitations

Despite the strong predictive success of the models there are limitations in the project, which include: 

- not including the use of weather data
- not including any information regarding holidays
- only testing two models; and not implementing real-time APIs.

These limitations present opportunities for future improvements to be made.


---

# 13. Future Research Directions

Several improvements can be explored in future work.

- Add weather-related features
- Include holiday and event information
- Explore deep learning models such as LSTM
- Integrate real-time electricity demand APIs
- Deploy the dashboard online for public access

These improvements can help build a more advanced and production-ready forecasting system.

---

# 14. References

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
