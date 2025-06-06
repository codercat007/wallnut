import streamlit as st


import pymongo
from pymongo import MongoClient
import certifi

ca = certifi.where()

cluster = MongoClient("mongodb+srv:###url",tlsCAFile=ca)
db = cluster['test']
collection = db['logindetails']

st.set_page_config(
    page_title="Login/Signup"
)

st.session_state['logged_in'] = False
st.session_state['user'] = "blank asf"


st.title("Welcome to Wallnut")



choice = st.selectbox('login/signup',['login','signup'])

if(choice=='login'):
    username = st.text_input('UserName')
    password = st.text_input('password',type='password')

    if st.button('login'):
        pas = collection.find_one({"UserName":username})
        if(pas is not None):
            if(pas['password']==password):
                st.success('logged in successfully')
                st.session_state['logged_in'] = True
                st.session_state['user'] = username
                st.switch_page('pages\LandingPage.py')
            else:
                st.error('invalid password')

        else:
            st.error("username not found, Please Sign Ups")



else:
    email = st.text_input('Email')
    password = st.text_input('password',type='password')
    uname = st.text_input('enter username')

    if st.button('create my account'):
        post = {"UserName":uname,"email":email,"password":password}
        collection.insert_one(post)
        st.success("account created successfully")
        st.markdown('please login with your email and password')
        st.balloons()
