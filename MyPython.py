import streamlit as st
import pandas as pd

st.title("Hello, Welcome to ScamGuard AI")

st.write("ScamGuard helps to prevent or detect **SCAM Messages**")

user_name = st.text_input("Enter User name")

user_age = st.slider("Enter your Age:", 0,100,50)

st.file_uploader("Choose a file")

user_movie=st.radio(

    "What's your favorite movie genre",

    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],

    captions=[

        "Laugh out loud.",

        "Get the popcorn.",

        "Never stop learning.",

    ],

)

if st.button("Submit"):

    st.write(f"user name : {user_name} and age : {user_age} and movie : {user_movie}")