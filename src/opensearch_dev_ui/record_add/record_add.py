import streamlit as st
from opensearch_dev_ui import OpenSearchClient, get_session_state, set_session_state
from record_add import Index_model_mapping

import streamlit_pydantic as sp

def record_add_tab():
    st.header("Adding record")

    set_session_state("tab", "record_add")
    client = get_session_state("client")

    if client is None:
        st.error("Please configure the connection first")
        return

    index_names = [index for index in client.get_all_indices() if index["index"] in Index_model_mapping]
    names = [index["index"] for index in index_names]
    index_name = st.selectbox("Select Index", names, key="record_add_index_selection")

    data = sp.pydantic_form(key=index_name, model=Index_model_mapping[index_name])
    if data:

        client.add_record(index_name, data.dict())
        st.success("Record added successfully")