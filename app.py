import streamlit as st
import re
import random
import string

# Custom CSS for Cyber Shield Theme
st.markdown("""
    <style>
        body {
            background-color: #black ; 
            color: #58a6ff;
            font-family: 'Arial', sans-serif;
        }
        .stTextInput, .stButton {
            border-radius: 10px;
            font-size: 16px;
        }
        .meter {
            width: 100%;
            height: 15px;
            background: #333;
            border-radius: 5px;
            margin-top: 10px;
            position: relative;
        }
        .fill {
            height: 100%;
            border-radius: 5px;
            transition: width 0.4s ease-in-out;
        }
        .weak { background: #ff4d4d; }
        .moderate { background: #ffcc00; }
        .strong { background: #4CAF50; }
        .footer {
            margin-top: 40px;
            padding: 10px;
            text-align: center;
            font-size: 14px;
            color: #8b949e;
        }
    </style>
""", unsafe_allow_html=True)

# Blacklisted passwords
COMMON_PASSWORDS = {"password", "123456", "qwerty", "password123", "abc123", "admin", "welcome"}

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []
    
    if password.lower() in COMMON_PASSWORDS:
        return 0, ["🚨 This password is too common. Choose something unique."]
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔴 Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("🔴 Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("🔴 Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("🔴 Include at least one special character (!@#$%^&*).")

    return score, feedback

# Function to generate a strong password
def generate_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for i in range(12))

# Streamlit UI
st.title("🔐 Password Strength Meter")
st.markdown("Enter a password below and check its security level.")

# Input field
password = st.text_input("Enter your password:", type="password")

# Password Strength Checking
if password:
    score, feedback = check_password_strength(password)
    
    # Define strength level
    strength = ["Weak", "Moderate", "Strong"][min(score, 2)]
    color_class = ["weak", "moderate", "strong"][min(score, 2)]
    strength_percentage = (score / 4) * 100  # Convert score to percentage

    # Strength meter
    st.markdown(f"""
        <div class="meter">
            <div class="fill {color_class}" style="width:{strength_percentage}%"></div>
        </div>
        <h3 style="color: {'#ff4d4d' if strength == 'Weak' else '#ffcc00' if strength == 'Moderate' else '#4CAF50'}">
            {strength} Password
        </h3>
    """, unsafe_allow_html=True)

    # Feedback
    if feedback:
        st.warning("\n".join(feedback))
    else:
        st.success("✅ Strong Password! Your password is secure.")

# Password Generator Button
if st.button("🔄 Generate Strong Password"):
    st.text(f"Suggested Password: {generate_password()}")

# Footer
st.markdown("""
    <div class="footer">
        📌 Made by <b>Yemna Mehmood❤</b> | <i>Password Strength Meter</i>
    </div>
""", unsafe_allow_html=True)
