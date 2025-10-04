import streamlit as st

st.title("Your Name's Resume")
st.header("Contact Information")
st.write("Email: your.email@example.com")
st.write("Phone: (123) 456-7890")
st.write("LinkedIn: linkedin.com/in/yourprofile")

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
