import streamlit as st

st.set_page_config(
    page_title="Ameer Zain's Resume",
    page_icon="✅",
    # layout="wide",
    initial_sidebar_state="expanded",
)

# Personal Information
st.title("Ameer Zain")
st.write("Software Developer")
st.write("Email: ameerzain04@gmail.com")
# st.write("Phone: (123) 456-7890")
st.write("LinkedIn: [linkedin.com/in/ameer-zain](https://www.linkedin.com/in/ameer-zain/)")

# Education
st.header("Education")
st.write("B.E, ECE")
st.write("Dhaanish Ahmed Institute of Technology")
st.write("Graduation: June 2022")

# Skills
st.header("Skills")
skills = ["Python", "C", "JavaScript", "HTML/CSS", "SQL", "Git", "UiPath"]
st.write(", ".join(skills))

# Work Experience
st.header("Work Experience")
st.write("Software Developer Intern")
st.write("Tech Company XYZ")
st.write("June 20XX - August 20XX")
st.write("- Developed and maintained features for web applications.")
st.write("- Collaborated with cross-functional teams to deliver high-quality software.")
st.write("- Participated in code reviews and provided constructive feedback.")

st.write("Junior Software Engineer")
st.write("Software Solutions Inc.")
st.write("September 20XX - Present")
st.write("- Contributed to the design and implementation of backend services.")
st.write("- Troubleshot and resolved software defects to improve application reliability.")
st.write("- Mentored junior developers and conducted knowledge-sharing sessions.")

# add more sections as needed (e.g., projects, certifications, etc.)

# Footer
st.text("Last updated: August 2023")