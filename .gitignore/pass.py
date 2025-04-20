import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", layout="centered")

# Styling
st.markdown("""
    <style>
        .good { color: green; font-weight: bold; }
        .ok { color: orange; font-weight: bold; }
        .weak { color: red; font-weight: bold; }
        .emoji { font-size: 24px; }
    </style>
""", unsafe_allow_html=True)

st.title("🔐 Password Strength Checker")

# Input field
password = st.text_input("Enter your password", type="password")

# Function to evaluate password strength
def check_strength(password):
    length = len(password) >= 8
    uppercase = re.search(r"[A-Z]", password)
    lowercase = re.search(r"[a-z]", password)
    digit = re.search(r"[0-9]", password)
    special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    checks = [length, uppercase, lowercase, digit, special]
    score = sum(bool(c) for c in checks)

    if score == 5:
        return "Strong", "🟢", "good"
    elif 3 <= score < 5:
        return "Moderate", "🟠", "ok"
    else:
        return "Weak", "🔴", "weak"

# Show result
if password:
    status, icon, style = check_strength(password)
    st.markdown(f'<div class="{style} emoji">{icon} Your password is <strong>{status}</strong>.</div>', unsafe_allow_html=True)

    # # Optional: Show breakdown
    # with st.expander("See detailed criteria"):
    #     st.write(f"✅ At least 8 characters: {'Yes' if len(password) >= 8 else 'No'}")
    #     st.write(f"✅ Includes uppercase letter: {'Yes' if re.search(r'[A-Z]', password) else 'No'}")
    #     st.write(f"✅ Includes lowercase letter: {'Yes' if re.search(r'[a-z]', password) else 'No'}")
    #     st.write(f"✅ Includes number: {'Yes' if re.search(r'[0-9]', password) else 'No'}")
    #     st.write(f"✅ Includes special character: {'Yes' if re.search(r'[!@#$%^&*(),.?\":{}|<>]', password) else 'No'}")

# Do the regex checks before the f-string
has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

with st.expander("See detailed criteria"):
    st.write(f"✅ At least 8 characters: {'Yes' if len(password) >= 8 else 'No'}")
    st.write(f"✅ Includes uppercase letter: {'Yes' if re.search(r'[A-Z]', password) else 'No'}")
    st.write(f"✅ Includes lowercase letter: {'Yes' if re.search(r'[a-z]', password) else 'No'}")
    st.write(f"✅ Includes number: {'Yes' if re.search(r'[0-9]', password) else 'No'}")
    st.write(f"✅ Includes special character: {'Yes' if has_special else 'No'}")

# else:
#     st.info("🔎 Start typing a password to see how strong it is.")

