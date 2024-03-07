import streamlit as st
import re
import pickle

def word_divider(words):
    char = []
    for i in words:
        char.append(i)
    return char

vectorizer = pickle.load(open("models/tdif.pkl", "rb"))

# Importing Logistic Regression
with open('models/lor.pkl', 'rb') as f:
    saved_data = pickle.load(f)
    
logreg = saved_data['model']
test_acc_lor = saved_data['test_accuracy']
train_acc_lor = saved_data['train_accuracy']

# Importing RandomForest
with open('models/rf.pkl', 'rb') as f:
    saved_data = pickle.load(f)

rfc = saved_data['model']
test_acc_rf = saved_data['test_accuracy']
train_acc_rf = saved_data['train_accuracy']

# Importing XGBoost
with open('models/xg.pkl', 'rb') as f:
    saved_data = pickle.load(f)

xgb = saved_data['model']
test_acc_xgb = saved_data['test_accuracy']
train_acc_xgb = saved_data['train_accuracy']

# Importing LGB
with open('models/lgb.pkl', 'rb') as f:
    saved_data = pickle.load(f)

lgb = saved_data['model']
test_acc_lgb = saved_data['test_accuracy']
train_acc_lgb = saved_data['train_accuracy']


def is_valid_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[!@#$%^&*]', password):
        return False
    return True


def preprocess_password(password):
    password = password.lower()
    password = re.sub(r'[^\w\s]', '', password)
    return password


def predict_password_strength_logreg(password, vectorizer, logreg):
    password_preprocessed = preprocess_password(password)
    password_vectorized = vectorizer.transform([password_preprocessed])
    password_strength = logreg.predict(password_vectorized)[0]
    return password_strength


def predict_password_strength_randomforest(password, vectorizer, rfc):
    password_preprocessed = preprocess_password(password)
    password_vectorized = vectorizer.transform([password_preprocessed])
    ps = rfc.predict(password_vectorized)[0]
    return ps

def predict_passwd_strength_xgBoost(password, vectorizer, xgb):
    password_preprocessed = preprocess_password(password)
    password_vectorized = vectorizer.transform([password_preprocessed])
    ps = xgb.predict(password_vectorized)[0]
    return ps

def predict_passwd_strength_lgb(password, vectorizer, lgb):
    password_preprocessed = preprocess_password(password)
    password_vectorized = vectorizer.transform([password_preprocessed])
    ps = lgb.predict(password_vectorized)[0]
    return ps

def main():
    st.set_page_config(
        page_title="Password Strength Tester",
        page_icon="🔐",
        layout="wide"
    )
    
    st.markdown(
        """
        <style>
            [title="Show password text"] {
                display: none;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    st.title("Password Strength Tester")

    st.sidebar.title("Navigation")
    app_mode = st.sidebar.selectbox(
        "Please select a page",
        ["Home", "Machine Learning Models"]
    )

    if app_mode == "Home":
        if "password" not in st.session_state:
            st.session_state["password"] = ""
        if "userName" not in st.session_state:
            st.session_state["userName"] = ""
        if "yob" not in st.session_state:
            st.session_state["yob"] = ""
        if "mother_name" not in st.session_state:
            st.session_state["mother_name"] = ""
        if "father_name" not in st.session_state:
            st.session_state["father_name"] = ""

    st.subheader("Enter your Name")
    userName = st.text_input("Enter your Name", value=st.session_state.get("userName", ""))
    st.session_state["userName"] = userName

    st.subheader("Please enter your birth year.")
    yob = st.text_input("Enter birth Year", value=st.session_state.get("yob", ""))
    st.session_state["yob"] = yob

    st.subheader("Enter your Mother's Name")
    mother_name = st.text_input("Enter your Mother's Name", value=st.session_state.get("mother_name", ""))
    st.session_state["mother_name"] = mother_name

    st.subheader("Enter your Father's Name")
    father_name = st.text_input("Enter your Father's Name", value=st.session_state.get("father_name", ""))
    st.session_state["father_name"] = father_name

    st.subheader("Enter a password to check the strength of it.")
    password = st.text_input("Password", type="password", value=st.session_state.get("password", ""))
    st.session_state["password"] = password

    st.subheader("Confirm your Password!")  
    confirm_password = st.text_input("Confirm Password", type="password", value=st.session_state.get("conf_pass", ""))
    st.session_state["conf_pass"] = confirm_password
    
    password_strength_lor = predict_password_strength_logreg(password, vectorizer, logreg)
    password_strength_rfc = predict_password_strength_randomforest(password, vectorizer, rfc)
    password_strength_xgb = predict_passwd_strength_xgBoost(password,vectorizer,xgb)
    password_strength_lgb = predict_passwd_strength_lgb(password,vectorizer,lgb)
    
    password_strength_dict = {0: "Weak", 1: "Medium", 2: "Strong"}
    password_strength_lor_str = password_strength_dict[password_strength_lor]
    password_strength_rfc_str = password_strength_dict[password_strength_rfc]
    password_strength_xgb_str = password_strength_dict[password_strength_xgb]
    password_strength_lgb_str = password_strength_dict[password_strength_lgb]
    
    if app_mode == "Home":
        if st.button("Check Password Strength"):
            if not userName or not yob or not mother_name or not father_name:
                st.warning("Please enter your Name, Birth Year, Mother's Name, and Father's Name.")
            elif not password:
                st.warning("Please enter a password.")
            elif userName in password:
                st.warning("Your password cannot contain your username.")
            elif yob in password:
                st.warning("Your password cannot contain your year of birth.")
            elif mother_name in password:
                st.warning("Your password cannot contain your mother's name.")
            elif father_name in password:
                st.warning("Your password cannot contain your father's name.")
            elif not is_valid_password(password):
                st.warning("Please enter a valid password. It should contain at least 8 characters, "
                        "1 uppercase letter, 1 number, and 1 special character (!@#$%^&*).")
            elif password != confirm_password:
                st.warning("Confirmed password does not match the entered password.")
            else:
                st.success("Password strength checked successfully!")
                
                st.write(f"Password Strength (Logistic Regression): {password_strength_lor_str}")
                st.write(f"Password Strength (Random Forest): {password_strength_rfc_str}")
                st.write(f"Password Strength (XGBoost): {password_strength_xgb_str}")
                st.write(f"Password Strength (LightGradientBoost): {password_strength_lgb_str}")


    elif app_mode == "Machine Learning Models":
            st.header("Machine Learning Models")

            st.subheader("Logistic Regression Model")
            st.write(f"Test Accuracy: {round(test_acc_lor, 2)}%")
            st.write(f"Train Accuracy: {round(train_acc_lor, 2)}%")
            st.write(f"Password Strength : {password_strength_lor_str}")

            st.subheader("Random Forest Model")
            st.write(f"Test Accuracy: {round(test_acc_rf, 2)}%")
            st.write(f"Train Accuracy: {round(train_acc_rf, 2)}%")
            st.write(f"Password Strength : {password_strength_rfc_str}")

            st.subheader("XGBoost Model")
            st.write(f"Test Accuracy: {round(test_acc_xgb, 2)}%")
            st.write(f"Train Accuracy: {round(train_acc_xgb, 2)}%")
            st.write(f"Password Strength : {password_strength_xgb_str}")
            
            st.subheader("Light Gradient Boost Model")
            st.write(f"Test Accuracy: {round(test_acc_lgb, 2)}%")
            st.write(f"Train Accuracy: {round(train_acc_lgb, 2)}%")
            st.write(f"Password Strength : {password_strength_lgb_str}")
            

            

if __name__ == "__main__":
    main()
