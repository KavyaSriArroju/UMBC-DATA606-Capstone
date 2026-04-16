# UMBC-DATA606-Capstone
# PJM Electricity Load Forecasting for Smart Grid Optimization

## 👩‍💻 Author
Kavya Sri Arroju  
UMBC Data Science Capstone – Spring 2026  

---

## 📌 Project Overview

This project focuses on forecasting hourly electricity demand in the PJM East region using historical load data.  

The goal is to build accurate predictive models that can help optimize energy usage, improve grid stability, and support smart grid systems.

---

## 🎯 Objective

The objective of this project is to predict future electricity demand (in megawatts) based on historical hourly data and time-based features.

---

## 📊 Dataset

- Dataset: PJM Hourly Energy Consumption  
- Source: Kaggle  
- Time Period: 2002 – 2018  
- Total Records: ~140,000  
- Target Variable: **PJME_MW (Electricity Load in MW)**  

---

## 🔍 Project Workflow

1. Data Collection  
2. Exploratory Data Analysis (EDA)  
3. Feature Engineering  
4. Model Building  
5. Model Evaluation  
6. Result Analysis  

---

## ⚙️ Feature Engineering

The following features were created:

- Hour of day  
- Day of week  
- Month and year  
- Weekend indicator  
- Cyclical features (sin/cos transformation)  
- Lag features (previous hour, previous day, previous week)  
- Rolling statistics (moving averages)  

---

## 🤖 Models Used

- Linear Regression  
- Random Forest Regressor  

---

## 📈 Evaluation Metrics

- Mean Absolute Error (MAE)  
- Root Mean Squared Error (RMSE)  
- R² Score  

---

## 📊 Results

| Model | MAE | RMSE | R² |
|------|-----|------|----|
| Linear Regression | 777 | 994 | 0.976 |
| Random Forest | 287 | 396 | 0.996 |

👉 The Random Forest model significantly outperformed Linear Regression and provided highly accurate predictions.

---

## 📌 Key Findings

- Electricity demand shows strong hourly, weekly, and seasonal patterns  
- Feature engineering improved model performance significantly  
- Tree-based models capture complex patterns better than linear models  
- Random Forest achieved near-perfect prediction accuracy  

---

## 📁 Repository Structure
