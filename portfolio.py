import streamlit as st

projects = [
    {
        "title": "Project 1: Data Analysis",
        "description": "Performed data analysis on a dataset of customer behavior.",
        "technologies": "Python, Pandas, Matplotlib",
    },
    {
        "title": "Project 2: Machine Learning",
        "description": "Developed a machine learning model for image classification.",
        "technologies": "Python, TensorFlow, Scikit-learn",
    },
    {
        "title": "Project 3: Web Development",
        "description": "Built a responsive website for a local business using HTML and CSS.",
        "technologies": "HTML, CSS",
    },
]

st.title("My Portfolio")
st.write("Welcome to my portfolio! Here are some of the projects I've worked on:")

for project in projects:
    st.write(f"### {project['title']}")
    st.write(project['description'])
    st.write(f"**Technologies used:** {project['technologies']}")

    st.write("---")
