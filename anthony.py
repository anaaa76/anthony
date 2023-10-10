import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


# Specify the path to your Excel file
csv_file_path = 'amazon.csv'

# Read data from the Excel file into a Pandas DataFrame
df = pd.read_csv(csv_file_path)

# Now you can work with the data in the DataFrame 'df'
# For example, you can print the first few rows of the DataFrame

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd



# Convert 'rating' column to numeric
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
# Convert 'rating_count' column to numeric after removing commas
df['rating_count'] = df['rating_count'].str.replace(',', '').astype(float)

# Streamlit app
st.title('Interactive Visualizations')

# Sidebar with interactive widgets
category_filter = st.sidebar.selectbox('Select Category:', df['category'].unique())
rating_slider = st.sidebar.slider('Select Minimum Rating:', min_value=0.0, max_value=5.0, step=0.1, value=0.0)

# Handle NaN values (if needed)
# df = df.dropna(subset=['rating'])

filtered_df = df[(df['category'] == category_filter) & (df['rating'] >= rating_slider)]

# Bar chart
fig2 = px.bar(filtered_df, x='rating', y='discounted_price', title='Bar Chart')
fig2.update_xaxes(title_text='Rating')
fig2.update_yaxes(title_text='Rating')

import streamlit as st
import plotly.express as px
import pandas as pd

# Streamlit app
st.title('Interactive Histogram')

# Add a slider to interactively change rating_count
# Add a slider to interactively change rating_count
rating_count = st.slider('Select Rating Count', min_value=0, max_value=int(df['rating_count'].max()), value=int(df['rating_count'].max()))

# Filter the DataFrame based on the selected rating_count
filtered_df = df[df['rating_count'] >= rating_count]

# Create a histogram
fig = px.histogram(filtered_df, x='rating_count', title='Rating Count Histogram')

# Show the plot
st.plotly_chart(fig)


# Show the visuals
st.plotly_chart(fig2)
