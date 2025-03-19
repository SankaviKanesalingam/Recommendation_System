

import streamlit as st
import pandas as pd

# Load the data from the CSV file
df = pd.read_csv('C:\\Users\\sankavi\\OneDrive\\Desktop\\Tourist_Guide\\Recommendation_System\\Data_for_Tourist.csv')

# Streamlit page configuration
st.set_page_config(page_title="Sri Lanka Tourist Guide", layout="wide")

# Title and Styling
st.markdown("<h1 style='text-align: center; color: #1E88E5;'>Sri Lanka Tourist Guide</h1>", unsafe_allow_html=True)

# Sidebar for filters
st.sidebar.header("🔍 Filter Places Based on Your Interests")

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
st.subheader(f"🌍 Recommended Places for {age_group} in {category}")

# Generate clickable Google Maps links
def generate_map_link(lat, lon):
    return f"https://www.google.com/maps?q={lat},{lon}"

# Display places as a responsive grid
cols = st.columns(3)  # 3-column layout

for index, row in filtered_data.iterrows():
    google_maps_link = generate_map_link(row['Latitude'], row['Longitude'])
    with cols[index % 3]:  # Distribute cards in 3 columns
        st.markdown(f"""
            <div style="border: 1px solid #ddd; border-radius: 10px; padding: 10px; margin: 10px; text-align: center; background-color: #f9f9f9;">
                <h4 style="color: #1E88E5;">{row['Name']}</h4>
                <p><strong>Category:</strong> {row['Category']}</p>
                <p style="color: #1E88E5;"><strong>Rating:</strong> ⭐ {row['Rating']}</p>
                <a href="{google_maps_link}" target="_blank" style="color: #D32F2F; font-weight: bold;">📍 View on Google Maps</a>
            </div>
        """, unsafe_allow_html=True)
