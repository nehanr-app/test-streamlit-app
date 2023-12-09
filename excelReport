import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# File path to your Excel file
file_path = "calibration_report.xlsx"  # Update this with your file path

# Read Excel file
try:
    data = pd.read_excel(file_path)

    # Show data
    st.write("Data from Excel:")
    st.write(data)

    # Select columns for plotting
    columns = data.columns.tolist()
    x_axis = st.selectbox('Select X-axis:', columns)
    y_axis = st.selectbox('Select Y-axis:', columns)

    # Plotting based on user selection
    if st.button("Plot Graph"):
        fig, ax = plt.subplots()
        ax.scatter(data[x_axis], data[y_axis])
        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)
        ax.set_title(f'{x_axis} vs {y_axis}')
        st.pyplot(fig)

except Exception as e:
    st.write("Error reading file:", e)
