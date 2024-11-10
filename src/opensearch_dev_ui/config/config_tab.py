import streamlit as st
from opensearch_dev_ui import OpenSearchClient, set_session_state

def config_tab():
    st.header("Configuration")
    st.write("Endpoint")
    st.text_input("endpoint", value="http://localhost:9200", key="endpoint")
    st.write("Username")
    st.text_input("username", value="admin", key="username")
    st.write("Password")
    st.text_input("password", type="password", value="admin", key="password")

    # button to test connection
    if st.button("Test Connection"):
        set_session_state("client", OpenSearchClient(
            st.session_state["endpoint"], st.session_state["username"], st.session_state["password"]
        ))
        response = st.session_state["client"].test_connection()
        # display response
        st.write(response)
        st.success("Connection successful")