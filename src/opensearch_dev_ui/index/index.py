import streamlit as st
from opensearch_dev_ui import OpenSearchClient, get_session_state, set_session_state

def index_tab():
    st.header("Index")

    client = get_session_state("client")
    if client is None:
        st.error("Please configure the connection first")
        return
    
    all_indices = client.get_all_indices()


    col1, col2 = st.columns(2)

    with col1:
        
        index_names = [index["index"] for index in all_indices]
        selected_index = index_names[0] if index_names else None
        for index in index_names:
            if st.button(index):
                selected_index = index
    with col2:
        st.write(f"Selected Index: {selected_index}")
        if selected_index is not None:
            index_info = client.get_index_info(selected_index)
            st.write(index_info)
            
            if st.button("View Data"):
                set_session_state("selected_index", selected_index)
                st.experimental_rerun()
            
            if st.button("Edit Mapping"):
                st.write("Edit Mapping functionality to be implemented")
            
            if st.button("Clone Index"):
                st.write("Clone Index functionality to be implemented")
            
            if st.button("Delete Index"):
                st.write("Delete Index functionality to be implemented")
