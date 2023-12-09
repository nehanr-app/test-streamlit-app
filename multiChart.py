import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# File path to your Excel file
file_path = "calibration_report.xlsx"  # Update this with your file path

# Read Excel file
try:
    # data = pd.read_excel(file_path)
    df = pd.read_excel(file_path)

    # Show data
    st.write("Data from Excel:")
    st.write(df)

    # Select columns for plotting
    columns = df.columns.tolist()

    selected_columns = st.multiselect('Select columns for plotting:', columns)
    x_axis = st.selectbox('Select X-axis:', selected_columns)
    y_axis = st.selectbox('Select Y-axis:', columns)

    # x_axis = st.selectbox('Select X-axis:', columns)
    # y_axis = st.selectbox('Select Y-axis:', columns)

    chart_type = st.selectbox("Select Chart Type", ["Line Chart", "Bar Chart", "Scatter Plot"])

    if chart_type == "Line Chart":
        # Line chart
        fig = px.line(df, x=x_axis, y=y_axis)
        st.plotly_chart(fig, use_container_width=True)
    elif chart_type == "Bar Chart":
        # Bar chart
        fig = px.bar(df, x=x_axis, y=y_axis)
        st.plotly_chart(fig, use_container_width=True)
    elif chart_type == "Scatter Plot":
        # Scatter plot
        fig = px.scatter(df, x=x_axis, y=y_axis)
        st.plotly_chart(fig, use_container_width=True)
    elif chart_type == "Pi Plot":
        # Scatter plot
        fig = px.scatter(df, x=x_axis, y=y_axis)
        st.plotly_chart(fig, use_container_width=True)

    # Plotting based on user selection
    # if st.button("Plot Graph") and len(selected_columns) > 1:
    #     fig, ax = plt.subplots()
    #     for column in selected_columns:
    #         ax.plot(data.index, data[column], label=column)
    #     ax.set_xlabel(x_axis)
    #     ax.set_ylabel(y_axis)
    #     ax.legend()
    #     ax.set_title('Multiple Columns Plot')
    #     st.pyplot(fig)
    # elif len(selected_columns) <= 1:
    #     st.write("Please select at least two columns for plotting.")


except Exception as e:
    st.write("Error reading file:", e)
