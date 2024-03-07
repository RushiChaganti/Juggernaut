import streamlit as st
st.set_page_config(
    page_title="About Us",
    page_icon="😊",
)

# Define page content
def about_us():
    st.title("About Us")
    st.write("We are a group of students and one supervisor working on a project together.")
    st.write("Here's some information about each team member:")
    # Define team member info
    team_members = [
        {
            
            "name": "Rushi Chaganti",
            "role": "Student",
            "bio": "I'm a Chandigarh University student with a passion for technology. Python, AWS, Linux, C, and C++ are some of my skills.",
        },
        {
            "name": "Shiva Karthik",
            "role": "Student",
            "bio": "I'm a student at Chandigarh University passionate for Machine learning and web development.",
        },
        {
            "name": "Rithish",
            "role": "Student",
            "bio": "I'm a student at Chandigarh University passionate for Machine learning and Ui design.",
        },
        {
            "name": "Santosh",
            "role": "Student",
            "bio": "I'm a sophomore, student at Chandigarh University. Passionate in web development and machine learning.",
        },
        {
            "name": "Dr. Deepak Upadhyay",
            "role": "Supervisor",
            "bio": "Dr. Deepak Upadhyay  is an associate professor of computer science at Chandigarh University. He research interests include Artificial intelligence, Internet of thing and cybersecurity.",
        },
    ]
    # Display team member info
    for member in team_members:
        st.subheader(member["name"])
        st.write(f"**Role:** {member['role']}")
        st.write(member["bio"])

about_us()