import streamlit as st


def set_session_state(key, value):
    st.session_state[key] = value

def get_session_state(key):

    if key in st.session_state:
        return st.session_state[key]
    
    return None