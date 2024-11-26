# Writing a Streamlit demo prototype for the interactive app

streamlit_code = """
import streamlit as st
import pandas as pd

# Sample data for the spreadsheet
data = {
    "Load #": [1, 2, 3, 4, 5],
    "Pickup City": ["Los Angeles", "San Diego", "San Francisco", "Fresno", "Sacramento"],
    "Delivery City": ["Phoenix", "Las Vegas", "Portland", "Seattle", "Denver"],
    "Weight": [500, 1200, 800, 450, 1000],
    "Cubes": [50, 120, 80, 45, 100],
    "Status": ["Pending", "Shipped", "Pending", "Delivered", "Pending"],
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Set up the main layout
st.title("Load Management Dashboard")

# Display the spreadsheet
st.subheader("Spreadsheet View")
selected_load = st.selectbox("Select a Load to View Details", options=df["Load #"])

st.dataframe(df)

# Display detailed popup for the selected load
st.subheader(f"Details for Load #{selected_load}")
load_data = df[df["Load #"] == selected_load].iloc[0]

st.text(f"Pickup City: {load_data['Pickup City']}")
st.text(f"Delivery City: {load_data['Delivery City']}")
st.text(f"Weight: {load_data['Weight']} lbs")
st.text(f"Cubes: {load_data['Cubes']} cu ft")
st.text(f"Status: {load_data['Status']}")

# File upload section
st.subheader("Upload Related PDFs")
uploaded_files = st.file_uploader("Upload PDFs for this Load (BOL, POD, Packing List)", accept_multiple_files=True)

if uploaded_files:
    st.write("Uploaded Files:")
    for uploaded_file in uploaded_files:
        st.text(f"- {uploaded_file.name}")

# "Bill to" section
st.subheader("Bill To")
st.text("Customer Name: Example Customer")
st.text("Address: 1234 Example St, Example City, EX 12345")
st.text("Invoice: $1500")
"""

# Save the script to a file
file_path = "/mnt/data/Streamlit_Load_Management_Demo.py"
with open(file_path, "w") as file:
    file.write(streamlit_code)

file_path

streamlit run Streamlit_Load_Management_Demo.py
