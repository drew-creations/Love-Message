__author__ = 'Andrew Pelikan'
import streamlit as st

st.title("A Message For You")

st.write("Wow! I can't believe you're here!")

st.write("I've been waiting for so long...")

st.write("Just to tell you...")

evaluation = st.text_input("Hello? Are you still there...")

if evaluation.lower() == "yes":

    st.write("Oh, that's good to hear. It's lonely here in this place.")

    st.write("Anyways, I just wanted to tell you that I love you. With all of my heart. Until the end of time.")
