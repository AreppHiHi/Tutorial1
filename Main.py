import streamlit as st

col1, col2 = st.columns([1, 3])

with col1:
    st.image("1 diagram.png", width=180)  # Replace with your image file name

with col2:
    st.title("Ariff Zakwan")
    st.markdown("""
    **📍 Location:** Johor, Malaysia  
    **📧 Email:** ariffzakwan@example.com  
    **📞 Phone:** +60 12-345 6789  
    **🔗 LinkedIn:** [linkedin.com/in/ariffzakwan](https://linkedin.com/in/ariffzakwan)  
    **💻 GitHub:** [github.com/ariffzakwan](https://github.com/ariffzakwan)
    """)



st.header("Education")
st.write("Degree, University Name, Year")

st.header("Work Experience")
st.write("Job Title, Company Name, Year")
st.write("- Description of responsibilities and achievements")

st.header("Skills")
st.write("- Skill 1")
st.write("- Skill 2")

st.header("🎓 Education")
st.markdown("""
**Bachelor of Computer Science (Software Engineering)**  
_Universiti Teknologi Malaysia (UTM)_ | 2021 – 2025  
- Focus Areas: Machine Learning, Web Development, Cloud Computing  
- Final Year Project: *MedicGo – A Student-Centered Healthcare App*
""")

st.header("Projects")
st.write("Project Name: Description")
