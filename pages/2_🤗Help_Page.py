import streamlit as st

def display_help():
    st.title("Welcome to the Password Strength Checker!")
    st.write("This is a help page which will guide you in our website. In a nutshell, this website is used to check the strength of your password. We do not store your password in any database.")

    st.write("To achieve this, we are using machine learning algorithms which will predict your password strength based on the following criteria:")
    st.write("1. Password length should be above or equal to 8 characters.")
    st.write("2. Password should contain at least one uppercase character.")
    st.write("3. Password should contain at least one special character.")
    st.write("4. Password should contain at least one number.")
    st.write("These conditions must be met before the password strength can be verified using machine learning. Additionally, we will check if your password contains your year of birth or username.")

    st.write("Once the above criteria have been met, we will predict the strength of your password using machine learning. You can choose Machine Learning Models page to see the accuracy of the models")
    
if __name__ == '__main__':
    display_help()