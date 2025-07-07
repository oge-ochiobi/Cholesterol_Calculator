# create a cholestrol calculator #

#LDL = int(input("Your LDL in mg/dL: "))
#HDL = int(input("Your HDL in mg/dL: "))
#Trigycerides = int(input("Your Triglycerides in mg/gL: "))
#Total_Cholesterol = round(LDL + HDL + (Trigycerides / 5), 2)
#print("Your Total Cholesterol is: ", Total_Cholesterol, "mg/dL") 
#if Total_Cholesterol > 0 :
#    if Total_Cholesterol < 200:
#        print("Desirable Total Cholesterol")
#    elif Total_Cholesterol <=239:
#        print("Borderline High")
#    else:
#        print("High")
        

import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Cholesterol Checker",
    layout="centered"
)

# 🎨 Inject Custom CSS
st.markdown("""
    <style>
    body {
        background-color: #0f3d3e; /* dark teal/green */
        color: #ffffff;
        font-family: 'Segoe UI', sans-serif;
    }
  
    
    .stApp {
        background-color: #1f595c;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 0 12px rgba(0, 255, 200, 0.1);
        color: white;
    }

    h1 {
        color: #d72638;
    }

    .css-18e3th9 {
        background-color: #fff0f3 !important;
    }

    .stButton>button {
        background-color: #f67280;
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.5rem 1rem;
        transition: 0.3s ease;
    }

    .stButton>button:hover {
        background-color: #c94c66;
    }
    </style>
""", unsafe_allow_html=True)

# Title and subtitle
st.title("💉 Cholesterol Checker")
st.subheader("Get a quick overview of your heart health with personalized advice.")

# Input fields
name = st.text_input("Your Name")
age = st.number_input("Age", min_value=1, max_value=120)
gender = st.selectbox("Gender", ["Select", "Female", "Male", "Other"])
total_chol = st.number_input("Total Cholesterol (mg/dL)", min_value=0)
hdl = st.number_input("HDL (Good Cholesterol - mg/dL)", min_value=0)
ldl = st.number_input("LDL (Bad Cholesterol - mg/dL)", min_value=0)

# Button
if st.button("🩺 Check My Cholesterol"):
    if name and gender != "Select":
        st.success(f"Hello {name}, here’s what your numbers say:")

        if total_chol < 200:
            st.info("✅ **Desirable Total Cholesterol**")
            st.markdown("""
                **💡 Tips:**  
                - Keep eating heart-friendly foods  
                - Exercise regularly  
                - Monitor cholesterol yearly
            """)
        elif 200 <= total_chol <= 239:
            st.warning("⚠️ **Borderline High Cholesterol**")
            st.markdown("""
                **💡 Tips:**  
                - Reduce red meat & fried foods  
                - Eat more oats, beans, and fiber  
                - Schedule a recheck in 3-6 months
            """)
        else:
            st.error("❗ **High Cholesterol Detected**")
            st.markdown("""
                **💡 Tips:**  
                - Limit saturated fat  
                - Adopt a Mediterranean diet  
                - Consult a healthcare professional
            """)

        if hdl > 60:
            st.success("🌟 Excellent HDL! Protective for heart health.")
        elif hdl < 40:
            st.warning("⚠️ Low HDL. Increase physical activity and healthy fats.")

        if ldl > 130:
            st.warning("⚠️ High LDL. Cut back on saturated and trans fats.")
    else:
        st.error("Please fill in all required fields.")
