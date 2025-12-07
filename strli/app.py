import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("C:\\manju\\app_cre\\my_pro1\\strli\\employee_performance.csv") 

# Convert the column to a numeric type, forcing errors to NaN if conversion fails
df["Performance_Score"] = pd.to_numeric(df["Performance_Score"], errors='coerce')
# Fill NaNs with 0 or drop them if you prefer
df = df.dropna(subset=["Performance_Score"])

# Dashboard title 6666
st.title("📊 Employee Performance Dashboard")

# Show raw data
st.subheader("Dataset Preview")
st.dataframe(df)

# Filter by department
departments = df["Department"].unique()
selected_dept = st.selectbox("Select Department", departments)
filtered_df = df[df["Department"] == selected_dept]

st.subheader(f"Employees in {selected_dept}")
st.dataframe(filtered_df)

# --- 1. DATA PREPARATION (The Fix for the TypeError) ---

# Define the ordinal mapping for the Feedback_Rating column
rating_map = {
    'Poor': 1,
    'Needs Improvement': 2,
    'Good': 3,
    'Excellent': 4,
    'Outstanding': 5
}



## Chart: Performance_Score by Employee
st.subheader("Performance_Score")
fig1 = px.bar(
    filtered_df,
    x="Employee_ID",
    y="Performance_Score",
    color="Department",
    title="Performance_Score"
)
st.plotly_chart(fig1)


# --- CHART 2: SCATTER PLOT ---
st.subheader("Training Hours vs. Feedback_Rating")
# Use the full df for context in the scatter plot
fig2 = px.scatter(
    df,
    x="Training_Hours",
    y="Feedback_Rating",
    color="Department",
    # Note: size must be a numeric column, ensure 'Performance_Score' is numeric
    size="Performance_Score", 
    hover_data=["Employee_ID", "Performance_Score"]
)
st.plotly_chart(fig2, use_container_width=True)

# Apply the mapping to create a new numeric column
df['Rating_Numeric'] = df['Feedback_Rating'].map(rating_map)

# Define the list of numeric columns to be averaged
NUMERIC_COLS = [
    'Years_Experience',
    'Training_Hours',
    'Performance_Score',
    'Rating_Numeric' # Use the new numeric column
]

# --- 2. AGGREGATE THE DATA TO CALCULATE AVERAGES ---

# Group by 'Department' and calculate the mean of the selected numeric columns
department_summary = df.groupby('Department')[NUMERIC_COLS].mean().reset_index()

# Rename the encoded rating column back to a friendly name for the output
department_summary = department_summary.rename(columns={'Rating_Numeric': 'Avg_Feedback_Rating_Score'})

# --- 3. STREAMLIT DISPLAY (Adapted from your previous code) ---

st.subheader("Department Average Performance Metrics")
st.dataframe(department_summary)

# Now you can successfully plot the average rating using the new column
fig3 = px.bar(
    department_summary, # Use the aggregated DataFrame
    x="Department",
    y="Avg_Feedback_Rating_Score",
    title="Average Feedback Rating Score by Department"
)
st.plotly_chart(fig3, use_container_width=True)






