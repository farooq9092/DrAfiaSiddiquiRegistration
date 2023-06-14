import csv
import streamlit as st

# Set page config to wide layout
st.set_page_config(layout="wide")

def save_data(name, phone, email, cnic, province, district, education):
    with open("registration_data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, email, cnic, province, district, education])

def main():
    st.title("Dr. Afia Siddiqui Movement Registration Form")
    st.markdown("ڈاکٹر عافیہ صدیقی کی رہائی کے لیے تحریک")
    
    name = st.text_input("Name")
    phone = st.text_input("Phone")
    email = st.text_input("Email")
    cnic = st.text_input("CNIC")
    province = st.selectbox("Province", ["Punjab", "Sindh", "Khyber Pakhtunkhwa", "Balochistan", "Gilgit-Baltistan", "Kashmir"])
    
    # Add district options based on the selected province
    if province == "Punjab":
        district = st.selectbox("District", ["Lahore", "Faisalabad", "Rawalpindi", "Multan"])
    elif province == "Sindh":
        district = st.selectbox("District", ["Karachi", "Hyderabad", "Sukkur", "Larkana"])
    elif province == "Khyber Pakhtunkhwa":
        district = st.selectbox("District", ["Peshawar", "Abbottabad", "Swat", "Mardan"])
    elif province == "Balochistan":
        district = st.selectbox("District", ["Quetta", "Gwadar", "Khuzdar", "Turbat"])
    elif province == "Gilgit-Baltistan":
        district = st.selectbox("District", ["Gilgit", "Skardu", "Ghizer", "Hunza"])
    elif province == "Kashmir":
        district = st.selectbox("District", ["Muzaffarabad", "Mirpur", "Kotli", "Rawlakot"])
    
    education = st.selectbox("Education", ["Primary", "Metric", "Intermediate", "Bachelor", "Master", "Ph.D.", "Other"])
    
    if st.button("Submit"):
        if not name or not phone or not email or not cnic or not province or not district or not education:
            st.error("Please fill in all fields.")
        elif not check_cnic_exists(cnic):
            save_data(name, phone, email, cnic, province, district, education)
            st.success("Registration successful!")
        else:
            st.error("CNIC already registered.")
    
    # Display the CSV file in the browser
    with open("registration_data.csv", "r") as file:
        csv_data = file.read()
        st.markdown(f"<h2>CSV Data</h2>", unsafe_allow_html=True)
        st.code(csv_data, language="csv")
    
    # Download the CSV file
    st.markdown(f"<h2>Download CSV</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        <a href="registration_data.csv" download>
            <button type="button">Download</button>
        </a>
        """,
        unsafe_allow_html=True
    )

def check_cnic_exists(cnic):
    with open("registration_data.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if "CNIC" in row and row["CNIC"] == cnic:
                return True
        return False

if __name__ == "__main__":
    main()
