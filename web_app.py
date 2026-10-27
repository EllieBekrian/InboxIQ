import streamlit as st
from email_utils import analyse_email, validate_ai_response

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

        st.subheader("AI Response Validation")

        # Sample AI response (temporary)
        ai_data = {
            "priority": "High",
            "category": "Delivery",
            "sentiment": "Negative",
            "summary": "The customer reports a delayed order."
        }

        is_valid = validate_ai_response(ai_data)

        if is_valid:
            st.success("AI Response is valid!")

            st.write("Category:", ai_data["category"])
            st.write("Priority:", ai_data["priority"])
            st.write("Sentiment:", ai_data["sentiment"])
            st.write("Summary:", ai_data["summary"])

        else:
            st.error("AI Response is invalid!")