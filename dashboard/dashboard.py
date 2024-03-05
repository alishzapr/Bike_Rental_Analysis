import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load data from CSV file
bike_df = pd.read_csv("all_data.csv")

# Data preprocessing functions
def prepare_bike_data(df):
    # Perform any necessary data preprocessing steps
    return df

# Prepare bike data
bike_df = prepare_bike_data(bike_df)

# Ensure 'dteday' column is converted to datetime format
bike_df['dteday'] = pd.to_datetime(bike_df['dteday'])

# Define Streamlit sidebar
with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://github.com/dataprofessor/dashboard/blob/43b0c1cf6f7a231abb7a09b502af1daead4015c9/streamlit-logo-secondary-colormark-darktext.png?raw=true")
    st.title("Bike Rental Analysis")
    st.write("Select date range:")
    min_date = bike_df['dteday'].min()
    max_date = bike_df['dteday'].max()
    start_date = st.date_input("Start Date", min_value=min_date, max_value=max_date, value=min_date)
    end_date = st.date_input("End Date", min_value=min_date, max_value=max_date, value=max_date)

# Define Streamlit app content
st.header('Bike Rental Analysis Dashboard')

# Convert start_date and end_date to datetime objects
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

# Filter the data based on the selected date range
filtered_df = bike_df[(bike_df['dteday'] >= start_date) & (bike_df['dteday'] <= end_date)]

# Group by month and calculate total bike rentals
monthly_rentals = filtered_df.groupby(filtered_df['dteday'].dt.month)['cnt_day'].sum()

# Plotting the data
st.subheader("Monthly Bike Rentals")
fig, ax = plt.subplots()
ax.bar(monthly_rentals.index, monthly_rentals.values)
ax.set_xlabel('Month')
ax.set_ylabel('Total Bike Rentals')
ax.set_title('Monthly Bike Rentals')
st.pyplot(fig)

# Section 1: Total Bike Rentals by Weather Situation
st.subheader('Total Bike Rentals by Weather Situation')
weather_stats = bike_df.groupby("weathersit_day")["cnt_day"].sum().sort_values(ascending=False)
weather_labels = ['Clear', 'Mist', 'Light Rain']
fig, ax = plt.subplots()
ax.bar(weather_labels, weather_stats)
ax.set_title('Total Bike Rentals by Weather Situation')
ax.set_xlabel('Weather Situation')
ax.set_ylabel('Total Bike Rentals')
plt.xticks(rotation=0)
plt.ticklabel_format(style='plain', axis='y')
st.pyplot(fig)

# Section 2: Correlation Heatmap
st.subheader('Correlation Heatmap')
correlation_matrix = bike_df[['cnt_day', 'temp_day', 'hum_day', 'windspeed_day', 'weathersit_day']].corr()
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5, ax=ax)
ax.set_title('Correlation Heatmap')
plt.tight_layout()
st.pyplot(fig)

# Section 3: Total Bike Rentals per Month
st.subheader('Total Bike Rentals per Month')
monthly_labels = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}
monthly_rentals = bike_df.groupby(bike_df['dteday'].dt.month)['cnt_day'].sum()
monthly_rentals.index = monthly_rentals.index.map(monthly_labels)
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(monthly_rentals.index, monthly_rentals.values, marker='o', linestyle='-')
ax.set_title('Total Bike Rentals per Month')
ax.set_xlabel('Month')
ax.set_ylabel('Total Bike Rentals')
plt.xticks(rotation=45)
plt.ticklabel_format(style='plain', axis='y')
plt.grid(True)
st.pyplot(fig)


# Footer
st.caption('Copyright (c) Alishza Putri Rahmadina')
