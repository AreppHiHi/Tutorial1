import streamlit as st

col1, col2 = st.columns([1, 3])

with col1:
    st.image("WhatsApp Image 2025-10-04 at 20.26.39_393da4d3.jpg", width=180)  # Replace with your image file name

with col2:
    st.title("Ariff Zakwan")
    st.markdown("""
    **📍 Location:** KeLANTAN, Malaysia  
    **📧 Email:** S22B0022siswa@edu.my.com  
    **📞 Phone:** +60 1137309195
    **🔗 LinkedIn:** [linkedin.com/in/ariffzakwan](https://linkedin.com/in/ariffzakwan)  
    **💻 GitHub:** [github.com/ariffzakwan](https://github.com/ariffzakwan)
    """)

st.header("Education")
st.markdown("""
**Bachelor of Information Technologies with Honours (Artificial Intelligent)**  
_Universiti Malaysia Kelantan (UMK)_ | 2022 – 2026  
""")

st.header("Work Experience")
st.write("Sorting , JnT, 2024")
st.write("- Sorted and organized parcels based on destination and delivery zones")
st.write("- Scanned barcodes and updated delivery information in the system")

st.header("Skills")
st.write("- IOT and Hardware")
st.write("- Software Tool *Google Colab*")




