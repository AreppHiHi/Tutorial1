import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Ariff Zakwan | Resume",
    page_icon="💼",
    layout="centered"
)

# --- PROFILE SECTION ---
col1, col2 = st.columns([1, 3])

with col1:
    st.image("profile.jpg", width=180)  # replace with your profile image

with col2:
    st.title("Ariff Zakwan")
    st.markdown("""
    📧 **Email:** ariffzakwan@example.com  
    📞 **Phone:** +60 12-345 6789  
    🔗 **LinkedIn:** [linkedin.com/in/ariffzakwan](https://linkedin.com/in/ariffzakwan)  
    💻 **GitHub:** [github.com/ariffzakwan](https://github.com/ariffzakwan)
    """)

st.write("---")

# --- EDUCATION ---
st.header("🎓 Education")
st.write("""
**Bachelor of Computer Science (Software Engineering)**  
Universiti Teknologi Malaysia | 2021 – 2025  
- Focus: Machine Learning, Web Development, and Cloud Computing  
- Final Year Project: *MedicGo – A Student-Centered Healthcare App*
""")

# --- WORK EXPERIENCE ---
st.header("💼 Work Experience")
st.write("""
**Software Engineering Intern** – TechWave Solutions (June 2024 – Sept 2024)  
- Developed internal tools using Python and Streamlit  
- Collaborated with 5 developers in an Agile workflow  
- Enhanced API response time by 20% through code optimization
""")

st.write("""
**Freelance Web Developer** (2022 – Present)  
- Built responsive websites for small businesses using FlutterFlow and Firebase  
- Integrated REST APIs and Firebase Authentication  
- Delivered 6+ successful projects on schedule
""")

# --- SKILLS ---
st.header("🧠 Skills")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("- Python\n- Streamlit\n- FlutterFlow")
with col2:
    st.markdown("- Firebase\n- HTML/CSS/JS\n- SQL")
with col3:
    st.markdown("- Machine Learning\n- Agile Development\n- Team Collaboration")

# --- PROJECTS ---
st.header("🚀 Projects")
st.subheader("MedicGo – Student Healthcare App")
st.write("""
A healthcare mobile app built for university students to:
- Schedule clinic appointments easily  
- Access over-the-counter medicine services  
- Chat securely with campus doctors (teleconsultation feature)
""")

st.subheader("Smart Solar-Powered Surveillance System")
st.write("""
An IoT-based home security system powered by solar energy, using:
- ESP32-CAM for real-time facial recognition  
- Blynk app for remote monitoring  
- AI integration for smart alerts
""")

# --- ACHIEVEMENTS ---
st.header("🏅 Achievements")
st.write("""
- Winner, UTM Innovation Challenge 2024 (Smart Tech Category)  
- Dean’s List Award – 4 consecutive semesters  
- Certified in TensorFlow Developer Certificate (Google, 2023)
""")

# --- FOOTER ---
st.write("---")
st.markdown("""
💬 *“Passionate about building technology that improves everyday life through innovation, usability, and sustainability.”*  
© 2025 Ariff Zakwan
""")
