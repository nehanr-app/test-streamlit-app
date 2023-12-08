import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create some sample data
data = pd.DataFrame({
    'x': np.arange(100),
    'y': np.random.randn(100)
})

# Function to plot a line chart
def line_chart():
    fig, ax = plt.subplots()
    ax.plot(data['x'], data['y'])
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Sample Line Chart')
    st.pyplot(fig)

# Function to plot a histogram
def histogram():
    fig, ax = plt.subplots()
    ax.hist(data['y'], bins=20)
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram of Y values')
    st.pyplot(fig)

# Streamlit code
st.title('Graph Display App')

# Add a selectbox to choose the type of chart
chart_type = st.selectbox('Select chart type:', ['Line Chart', 'Histogram'])

# Display the selected chart
if chart_type == 'Line Chart':
    line_chart()
elif chart_type == 'Histogram':
    histogram()
