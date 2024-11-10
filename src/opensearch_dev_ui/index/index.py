import streamlit as st
from opensearch_dev_ui import OpenSearchClient, get_session_state, set_session_state


@st.dialog("Confirmation")
def delete_index_popup(index_names):
    client = get_session_state("client")
    index_name = st.selectbox("Select Index", index_names, key="delete_index_selection")
    st.write(f"Are you sure you want to delete {index_name}?")
    if st.button("Delete"):
        client.delete_index(index_name)
        st.rerun()


@st.dialog("Clone Index")
def clone_index_popup(index_names):
    client = get_session_state("client")
    index_name = st.selectbox("Select Index", index_names, key="clone_index_selection")
    st.write(f"Enter new index name to clone {index_name}")
    new_index_name = st.text_input("New Index Name")
    if st.button("Clone"):
        client.clone_index(index_name, new_index_name)
        st.rerun()

def index_tab():
    st.header("Index")

    set_session_state("tab", "index")
    client = get_session_state("client")
    if client is None:
        st.error("Please configure the connection first")
        return
    
    if st.button("Refresh Indices"):
        st.rerun()

    all_indices = client.get_all_indices()

    col1, col2 = st.columns(2)

    with col1:
        index_names = [index["index"] for index in all_indices]
        selected_index = index_names[0] if index_names else None
        for index in index_names:
            if st.button(index):
                selected_index = index
                set_session_state("selected_index", index)

    with col2:
        
        st.write(f"Selected Index: {selected_index}")
        if selected_index is not None:
            button_col = st.columns(4)
            with button_col[0]:
                if st.button("Refresh"):
                    st.rerun()
                
            with button_col[1]:
                if st.button("Edit Mapping"):
                    st.write("Edit Mapping functionality to be implemented")

            with button_col[2]:
                if st.button("Clone Index"):
                    clone_index_popup(index_names)

            with button_col[3]:
                if st.button("Delete Index"):
                    delete_index_popup(index_names)

            index_info = client.get_index_info(selected_index)
            container = st.container(border=True, height=500)
            container.write(index_info)
