import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="PJM Load Forecasting Dashboard", layout="wide")

st.title("⚡ PJM Electricity Load Forecasting Dashboard")
st.markdown("Interactive dashboard for electricity demand analysis, model comparison, and prediction.")

# Sidebar
st.sidebar.header("Dashboard Controls")
uploaded_file = st.sidebar.file_uploader("Upload featured_data.csv", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    try:
        df = pd.read_csv("featured_data.csv")
        st.sidebar.success("Using local featured_data.csv")
    except FileNotFoundError:
        st.warning("Please upload featured_data.csv to continue.")
        st.stop()

# Preprocessing
df["Datetime"] = pd.to_datetime(df["Datetime"])
df = df.sort_values("Datetime")

features = [
    "hour", "dayofweek", "month", "year", "is_weekend",
    "hour_sin", "hour_cos", "month_sin", "month_cos",
    "lag_1", "lag_24", "lag_168",
    "rolling_mean_24", "rolling_std_24"
]
target = "PJME_MW"

missing_cols = [col for col in features + [target] if col not in df.columns]
if missing_cols:
    st.error(f"Missing columns: {missing_cols}")
    st.stop()

# Sidebar filters
min_date = df["Datetime"].min().date()
max_date = df["Datetime"].max().date()

date_range = st.sidebar.date_input(
    "Select date range",
    [min_date, max_date],
    min_value=min_date,
    max_value=max_date
)

if len(date_range) == 2:
    start_date, end_date = date_range
    df = df[(df["Datetime"].dt.date >= start_date) & (df["Datetime"].dt.date <= end_date)]

rows_to_plot = st.sidebar.slider(
    "Rows to plot",
    min_value=100,
    max_value=min(2000, len(df)),
    value=min(300, len(df)),
    step=100
)

# Train/test split
X = df[features]
y = df[target]

split_index = int(len(df) * 0.8)
X_train = X.iloc[:split_index]
X_test = X.iloc[split_index:]
y_train = y.iloc[:split_index]
y_test = y.iloc[split_index:]
dates_test = df["Datetime"].iloc[split_index:]

# Models
lr = LinearRegression()
lr.fit(X_train, y_train)
lr_preds = lr.predict(X_test)

rf = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)
rf.fit(X_train, y_train)
rf_preds = rf.predict(X_test)

# Metrics
def get_metrics(y_true, y_pred):
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)
    return mae, rmse, r2

lr_mae, lr_rmse, lr_r2 = get_metrics(y_test, lr_preds)
rf_mae, rf_rmse, rf_r2 = get_metrics(y_test, rf_preds)

# Top KPI cards
current_actual = y_test.iloc[-1]
current_rf_pred = rf_preds[-1]
peak_load = y_test.max()
avg_load = y_test.mean()

c1, c2, c3, c4 = st.columns(4)
c1.metric("Current Actual Load", f"{current_actual:,.0f} MW")
c2.metric("Current RF Predicted Load", f"{current_rf_pred:,.0f} MW")
c3.metric("Peak Load", f"{peak_load:,.0f} MW")
c4.metric("Average Load", f"{avg_load:,.0f} MW")

# Demand status logic
if current_actual < avg_load * 0.90:
    demand_status = "Low"
    st.info("🔵 Demand Status: Low — current load is below the normal average range.")
elif current_actual <= avg_load * 1.10:
    demand_status = "Normal"
    st.success("✅ Demand Status: Normal — current load is within the expected range.")
elif current_actual <= avg_load * 1.20:
    demand_status = "High"
    st.warning("🟠 Demand Status: High — current load is above average and may indicate a peak period.")
else:
    demand_status = "Critical"
    st.error("🔴 Demand Status: Critical — current load is far above average and may increase grid stress.")

st.markdown(f"### Current Demand Level: **{demand_status}**")

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Model Comparison", "Predictions", "Insights"])

with tab1:
    st.subheader("Dataset Overview")
    st.dataframe(df.head())

    overview_fig = px.line(
        df.head(rows_to_plot),
        x="Datetime",
        y="PJME_MW",
        title="Electricity Load Over Time"
    )
    st.plotly_chart(overview_fig, use_container_width=True)

with tab2:
    st.subheader("Model Performance Comparison")

    metrics_df = pd.DataFrame({
        "Model": ["Linear Regression", "Random Forest"],
        "MAE": [lr_mae, rf_mae],
        "RMSE": [lr_rmse, rf_rmse],
        "R2": [lr_r2, rf_r2]
    })

    st.dataframe(metrics_df)

    metric_choice = st.selectbox("Select metric to compare", ["MAE", "RMSE", "R2"])

    comp_fig = px.bar(
        metrics_df,
        x="Model",
        y=metric_choice,
        color="Model",
        title=f"{metric_choice} Comparison"
    )
    st.plotly_chart(comp_fig, use_container_width=True)

with tab3:
    st.subheader("Actual vs Predicted Electricity Load")

    plot_df = pd.DataFrame({
        "Datetime": dates_test.iloc[:rows_to_plot],
        "Actual": y_test.iloc[:rows_to_plot].values,
        "Linear Regression": lr_preds[:rows_to_plot],
        "Random Forest": rf_preds[:rows_to_plot]
    })

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=plot_df["Datetime"], y=plot_df["Actual"], mode="lines", name="Actual"))
    fig.add_trace(go.Scatter(x=plot_df["Datetime"], y=plot_df["Linear Regression"], mode="lines", name="Linear Regression"))
    fig.add_trace(go.Scatter(x=plot_df["Datetime"], y=plot_df["Random Forest"], mode="lines", name="Random Forest"))

    fig.update_layout(
        title="Actual vs Predicted Electricity Load",
        xaxis_title="Datetime",
        yaxis_title="Load (MW)",
        hovermode="x unified"
    )
    st.plotly_chart(fig, use_container_width=True)

    pred_df = pd.DataFrame({
        "Datetime": dates_test.values,
        "Actual": y_test.values,
        "Linear_Regression_Predicted": lr_preds,
        "Random_Forest_Predicted": rf_preds,
        "RF_Error": y_test.values - rf_preds
    })

    st.subheader("Prediction Table")
    st.dataframe(pred_df.head(20))

    csv = pred_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Download Predictions CSV",
        data=csv,
        file_name="predictions.csv",
        mime="text/csv"
    )

with tab4:
    st.subheader("Feature Importance")
    importance_df = pd.DataFrame({
        "Feature": features,
        "Importance": rf.feature_importances_
    }).sort_values(by="Importance", ascending=False)

    importance_fig = px.bar(
        importance_df,
        x="Importance",
        y="Feature",
        orientation="h",
        title="Random Forest Feature Importance"
    )
    importance_fig.update_layout(yaxis=dict(categoryorder="total ascending"))
    st.plotly_chart(importance_fig, use_container_width=True)

    st.subheader("Prediction Error")
    error_df = pd.DataFrame({
        "Datetime": dates_test.iloc[:rows_to_plot],
        "Error": y_test.iloc[:rows_to_plot].values - rf_preds[:rows_to_plot]
    })

    error_fig = px.line(
        error_df,
        x="Datetime",
        y="Error",
        title="Random Forest Prediction Error Over Time"
    )
    st.plotly_chart(error_fig, use_container_width=True)

    st.markdown("### Key Insights")
    st.write("- Random Forest performs better than Linear Regression.")
    st.write("- Lag and rolling features are highly important.")
    st.write("- The model captures electricity demand trends very accurately.")
    st.write(f"- Current demand status is **{demand_status}**.")
