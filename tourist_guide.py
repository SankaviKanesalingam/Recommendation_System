import streamlit as st
import pandas as pd

# Load the data from the CSV file
df = pd.read_csv('C:\\Users\\sankavi\\OneDrive\\Desktop\\Tourist_Guide\\Recommendation_System\\Data_for_Tourist.csv')

# Streamlit page configuration
st.set_page_config(page_title="Sri Lanka Tourist Guide", layout="wide")

# Title
st.title("Sri Lanka Tourist Guide")

# Sidebar for user input
st.sidebar.header("Filter Places Based on Your Interests")

# Age Group Filter
age_group = st.sidebar.selectbox(
    "Select your age group", ['All', 'Adults', 'Kids', 'Seniors'])

# Category Filter
category = st.sidebar.selectbox(
    "Select your interest", ['Cultural', 'Wildlife', 'Historical', 'Beach', 'Adventure', 'Natural', 'Modern'])

# Filter the data based on user input
filtered_data = df[(df['Age_Group'] == age_group) | (df['Age_Group'] == 'All')]
filtered_data = filtered_data[filtered_data['Category'] == category]

# Show the results
st.subheader(f"Places to visit for {age_group} in the category {category}")
st.write(filtered_data[['Name', 'Category', 'Age_Group', 'Rating']])

# Bonus: Sorting by Rating
st.subheader("Sorted by Rating")
sorted_data = filtered_data.sort_values(by="Rating", ascending=False)
st.write(sorted_data[['Name', 'Category', 'Age_Group', 'Rating']])
