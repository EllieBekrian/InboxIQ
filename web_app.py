import streamlit as st
from email_utils import analyse_email


st.title("InboxIQ")

st.subheader("AI-Powered Customer Email Assistant")

st.write("Enter a customer email below to analyse it.")

email_text = st.text_area("Customer Email")

if st.button("Analyse Email"):
    if not email_text.strip():
        st.warning("Please enter an email first.")
    else:
        word_count, character_count = analyse_email(email_text)

        st.write("Email word count:", word_count)
        st.write("Email character count:", character_count)