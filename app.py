'''
Q3- PROJECT 2 
Build a Password Strength Meter in Python that evaluates a user's password based on security rules. The program will:

Analyze passwords based on length, character types, and patterns.
Assign a strength score (Weak, Moderate, Strong).
Provide feedback to improve weak passwords.
Use control flow, type casting, strings, and functions.
'''

import streamlit as st
import re

# Page Config
st.set_page_config(
    page_title="Password Strength Meter", 
    page_icon="🔐", 
    layout="centered", 
    initial_sidebar_state="collapsed"
)

# App Title with Inline CSS for Proper Styling
st.markdown(
    """
    <h1 style='text-align: center; color: #0078ff; font-size: 2em; font-weight: bold;'>
        Password Strength Meter 🔐
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown("""
## Welcome! 🚀
Use this tool to check your password strength and get security suggestions.
""")

# Password Input
password = st.text_input("🔑 Enter your password:", type="password")

# Initialize score and feedback
feedback = []
score = 0

if password:
    # Length Checking
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.") 

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # Special Character Check
    if re.search(r"[^\w]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (e.g., !@#$%^&*).")

    # Strength Rating & Progress Bar
    st.markdown("## Strength Rating:")
    st.progress(score / 5)

    if score >= 5:
        feedback.append("✅ Excellent Password! 💪")
    elif score >= 3:
        feedback.append("⚠️ Moderate Password - Consider improving it.")
    else:
        feedback.append("❌ Weak Password - Use the suggestions below.")

    # Display Suggestions
    if feedback:
        st.markdown("## Suggestions:")
        for suggestion in feedback:
            st.write(f"- {suggestion}")
else:
    st.info("Enter a password to get started!")

# Footer
st.write("Developed by Zahida Raees")
