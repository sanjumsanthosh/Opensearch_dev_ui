import streamlit as st
import json
from opensearch_dev_ui.config import config_tab
from opensearch_dev_ui.index import index_tab
from opensearch_dev_ui.explore import explore_tab
from opensearch_dev_ui.record_add import record_add_tab

def main():
    st.set_page_config(layout="wide")
    
    tabs = st.tabs(["Configuration", "Index", "Explore", "Record Add"])
    
    with tabs[0]:
        config_tab()

    with tabs[1]:
        index_tab()
    
    with tabs[2]:
        explore_tab()

    with tabs[3]:
        record_add_tab()


if __name__ == "__main__":
    main()