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
    selected_columns = st.multiselect('Select columns for plotting:', columns)
    y_axis = st.selectbox('Select Y-axis:', selected_columns)

    # x_axis = st.selectbox('Select X-axis:', columns)
    # y_axis = st.selectbox('Select Y-axis:', columns)

    # Plotting based on user selection
    if st.button("Plot Graph") and len(selected_columns) > 1:
        fig, ax = plt.subplots()
        for column in selected_columns:
            ax.plot(data.index, data[column], label=column)
        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)
        ax.legend()
        ax.set_title('Multiple Columns Plot')
        st.pyplot(fig)
    elif len(selected_columns) <= 1:
        st.write("Please select at least two columns for plotting.")


except Exception as e:
    st.write("Error reading file:", e)
