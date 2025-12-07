import streamlit as st
import pandas as pd
import plotly.express as px
import os

# --- Configuration and Setup ---
# Use the reliable path solution here
DATA_PATH = r"C:\manju\app_cre\my_pro1\employee_performance.csv"
st.set_page_config(layout="wide", page_title="Employee Performance Dashboard")

# --- 1. Data Loading ---
@st.cache_data
def load_data(path):
    # Check if the file exists before attempting to read
    if not os.path.exists(path):
        st.error(f"Error: File not found at {path}. Please check the file path.")
        return pd.DataFrame() # Return empty DataFrame on failure
    try:
        return pd.read_csv(path)
    except Exception as e:
        st.error(f"Error reading CSV file: {e}")
        return pd.DataFrame()

df = load_data(DATA_PATH)

# Check if data loaded successfully
if df.empty:
    st.stop() # Stop execution if data load failed

# --- 2. Sidebar Filters ---
st.sidebar.header("Filter Options")

# Department Filter
selected_departments = st.sidebar.multiselect(
    "Select Department:",
    options=df['Department'].unique(),
    default=df['Department'].unique()
)

# Experience Filter (Slider for numerical data)
min_exp = int(df['Years_Experience'].min())
max_exp = int(df['Years_Experience'].max())
exp_range = st.sidebar.slider(
    "Years of Experience Range:",
    min_value=min_exp,
    max_value=max_exp,
    value=(min_exp, max_exp)
)

# Apply Filters
filtered_df = df[
    (df['Department'].isin(selected_departments)) &
    (df['Years_Experience'] >= exp_range[0]) &
    (df['Years_Experience'] <= exp_range[1])
]

# --- 3. Main Dashboard Body ---
st.title("Employee Performance Analysis Dashboard 📈")
st.markdown("---")

## Key Metrics (KPIs)

total_employees = filtered_df.shape[0]
avg_score = filtered_df['Performance_Score'].mean()
attrition_rate = (filtered_df['Attrition'].value_counts(normalize=True).get('Yes', 0) * 100)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Total Employees", value=f"{total_employees}")

with col2:
    st.metric(label="Avg Performance Score", value=f"{avg_score:.2f}")

with col3:
    st.metric(label="Attrition Rate", value=f"{attrition_rate:.2f}%")

st.markdown("---")

## Performance Charts

# 1. Performance Distribution by Department (Bar Chart)
# Group the filtered data by Department and calculate the mean score
performance_by_dept = filtered_df.groupby('Department')[' Training_Hours].mean().reset_index()

fig_dept = px.bar(
    performance_by_dept,
    x="Department",
    y="Training_Hours",
    color="Department",
    title="Average Training Hours by Department",
    template="plotly_white"
)
st.plotly_chart(fig_dept, use_container_width=True)


# 2. Score vs. Experience (Scatter Plot)
fig_scatter = px.scatter(
    filtered_df,
    x="Years_Experience",
    y="Training_Hours",
    color="Feedback_Rating",
    hover_data=['Employee_ID'],
    title="Training Hours vs. Years of Experience",
    template="plotly_white"
)
st.plotly_chart(fig_scatter, use_container_width=True)

# 3. Raw Data View (Optional)
if st.checkbox('Show Raw Data'):
    st.subheader('Raw Data')
    st.dataframe(filtered_df)
# Example of creating a hypothetical column (if needed)
df['Training_Hours'] = df['Performance_Score'] * 10
# (Then you can use it in the px.bar function)    

