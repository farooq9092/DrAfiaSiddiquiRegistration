import csv
import streamlit as st

# Set page config to wide layout
st.set_page_config(layout="wide")

# Add CSS styling to set the background image and position the input fields
st.markdown(
    """
    <style>
    .container {
        position: relative;
        width: 100%;
        height: 100%;
    }
    .background-image {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1;
    }
    .form-container {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background-color: rgba(255, 255, 255, 0.8);
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
        z-index: 1;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def save_data(name, phone, email, cnic, province, district, education):
    with open("registration_data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, email, cnic, province, district, education])

def main():
    st.title("Dr. Afia Siddiqui Movement Registration Form")
    st.markdown("ڈاکٹر عافیہ صدیقی کی رہائی کے لیے تحریک")
    
    # Add your image file name in the background image URL
    image_file = "Aafia-Siddiqui.jpg"
    
    # Create a container for the background image and the form
    container = st.container()
    
    # Add the background image
    container.image(image_file, use_column_width=True, output_format="auto", 
                    caption="", clamp=False, channels="RGB")
    
    # Create a form container to position the input fields
    form_container = container.container()
    
    name = form_container.text_input("Name")
    phone = form_container.text_input("Phone")
    email = form_container.text_input("Email")
    cnic = form_container.text_input("CNIC")
    province = form_container.selectbox("Province", ["Punjab", "Sindh", "Khyber Pakhtunkhwa", "Balochistan", "Gilgit-Baltistan"])
    
    # Add district options based on the selected province
    if province == "Punjab":
        district = form_container.selectbox("District", ["Lahore", "Faisalabad", "Rawalpindi", "Multan"])
    elif province == "Sindh":
        district = form_container.selectbox("District", ["Karachi", "Hyderabad", "Sukkur", "Larkana"])
    elif province == "Khyber Pakhtunkhwa":
        district = form_container.selectbox("District", ["Peshawar", "Abbottabad", "Swat", "Mardan"])
    elif province == "Balochistan":
        district = form_container.selectbox("District", ["Quetta", "Gwadar", "Khuzdar", "Turbat"])
    elif province == "Gilgit-Baltistan":
        district = form_container.selectbox("District", ["Gilgit", "Skardu", "Ghizer", "Hunza"])
    
    education = form_container.selectbox("Education", ["Primary", "Metric", "Intermediate", "Bachelor", "Master", "Ph.D.", "Other"])
    
    if form_container.button("Submit"):
        if not name or not phone or not email or not cnic or not province or not district or not education:
            form_container.error("Please fill in all fields.")
        elif not check_cnic_exists(cnic):
            save_data(name, phone, email, cnic, province, district, education)
            form_container.success("Registration successful!")
        else:
            form_container.error("CNIC already registered.")

def check_cnic_exists(cnic):
    with open("registration_data.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if "CNIC" in row and row["CNIC"] == cnic:
                return True
        return False

if __name__ == "__main__":
    main()

