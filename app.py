import streamlit as st

st.set_page_config(page_title="Restaurant Reservation Bot", layout="centered")

# Initialize session state
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.reservation = {}

st.title("🍽️ Restaurant Reservation Chatbot")

def reset_chat():
    st.session_state.step = 0
    st.session_state.reservation = {}

with st.container():
    if st.session_state.step == 0:
        st.write("👋 Welcome to OceanView Restaurant! What's your name?")
        name = st.text_input("Your name", key="name_input")
        if name:
            st.session_state.reservation["name"] = name
            st.session_state.step = 1
            st.experimental_rerun()

    elif st.session_state.step == 1:
        st.write(f"Hi {st.session_state.reservation['name']}! What date would you like to book?")
        date = st.date_input("Select a date")
        if date:
            st.session_state.reservation["date"] = date.strftime("%Y-%m-%d")
            st.session_state.step = 2
            st.experimental_rerun()

    elif st.session_state.step == 2:
        st.write("What time would you like to reserve?")
        time = st.text_input("Reservation time (e.g. 7:00 PM)", key="time_input")
        if time:
            st.session_state.reservation["time"] = time
            st.session_state.step = 3
            st.experimental_rerun()

    elif st.session_state.step == 3:
        st.write("How many people in your party?")
        people = st.number_input("Party size", min_value=1, step=1)
        if people:
            st.session_state.reservation["people"] = int(people)
            st.session_state.step = 4
            st.experimental_rerun()

    elif st.session_state.step == 4:
        res = st.session_state.reservation
        st.success(f"✅ Reservation Confirmed!\n\n**Name:** {res['name']}\n\n**Date:** {res['date']}\n\n**Time:** {res['time']}\n\n**Party Size:** {res['people']}")
        st.button("Start Over", on_click=reset_chat)
