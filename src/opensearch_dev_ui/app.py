import streamlit as st
import json
from opensearch_dev_ui.config import config_tab
from opensearch_dev_ui.index import index_tab

def main():
    st.set_page_config(layout="wide")
    
    tabs = st.tabs(["Configuration", "Index"])
    
    with tabs[0]:
        config_tab()

    with tabs[1]:
        index_tab()



def json_editor_tab():
    st.header("JSON Editor")
    json_input = st.text_area("Edit JSON", "{}")
    if st.button("Validate JSON"):
        try:
            json.loads(json_input)
            st.success("Valid JSON")
        except json.JSONDecodeError:
            st.error("Invalid JSON")


if __name__ == "__main__":
    main()