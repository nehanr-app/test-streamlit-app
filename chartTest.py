import pandas as pd
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# def generateReport():
#     # Read data from Excel file into a pandas DataFrame
#     file_path = 'calibration_report.xlsx'  # Replace with your Excel file path
#     data = pd.read_excel(file_path)
#
#     # Assuming your Excel file has columns named 'Category' and 'Values'
#     gitCommits = data['Git Commits']
#     linesModified = data['Lines Modified']
#
#     # Create a bar plot using seaborn
#     plt.figure(figsize=(8, 6))
#     sns.barplot(x=linesModified, y=gitCommits)
#     # plt.bar(gitCommits, linesModified)
#     plt.title('Bar Plot from Excel Data')
#     plt.xlabel('Lines Modified')
#     plt.ylabel('Git Commits')
#     plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
#     plt.tight_layout()
#
#     plt.show()

def checkStreamlit():


    # Streamlit app title
    st.title('Excel Data Visualization App')

    # Upload Excel file
    uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx", "xls"])

    if uploaded_file is not None:
        try:
            # Read Excel file
            df = pd.read_excel(uploaded_file)

            st.write("Data from Excel:")
            st.write(df)

            st.subheader("Select columns for chart:")
            columns = df.columns.tolist()

            # Select columns for X and Y axes
            x_axis = st.selectbox("X-axis", columns)
            y_axis = st.selectbox("Y-axis", columns)

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

        except Exception as e:
            st.error("An error occurred: {}".format(e))
