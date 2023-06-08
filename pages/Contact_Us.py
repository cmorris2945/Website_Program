import streamlit as st
from send_email import send_email

st.header("Let Me Know If I Can Help You. Contact Me...")

with st.form(key ="email_forms"):
    user_email = st.text_input("PLEASE ENTER YOUR EMAIL ADDRESS BELOW: ")
    option = st.selectbox(
        'What job or topic would you like to discuss with me? '
        '(Select from the dropdown...)',
        ('Consulting', 'Contract Position', 'Temp Assignment', 'Permanent Placement'))



    raw_message = st.text_area("WRITE YOUR MESSAGE BELOW:")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
Concerning: {option}
{raw_message}"""
    button = st.form_submit_button()
    print(button)

    if button:
        st.write('You selected:', option)
        send_email(message)
        st.info("Great! We gotch your email! Someone will get back to you shortly... ")

