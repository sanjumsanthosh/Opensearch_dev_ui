import streamlit as st
from opensearch_dev_ui import get_session_state, set_session_state


@st.dialog("Visualize Data", width="large")
def data_visualizer_dialog(json_data):
    st.write(json_data)


def explore_tab():
    st.header("Explore")

    set_session_state("tab", "explore")

    client = get_session_state("client")
    if client is None:
        st.error("Please configure the connection first")
        return

    all_indices = client.get_all_indices()
    index_names = [index["index"] for index in all_indices]

    selected_index = st.selectbox("Select Index", index_names, key="explore_index_selection")
    set_session_state("selected_index", selected_index)

    if selected_index:
        response = client.search_index(selected_index)
        data = response.get("hits", {}).get("hits", [])
        if data:
            # _source colum is json data view it as json and add a button to view the data in popup
            data = [
                {
                    "index": hit["_index"],
                    "id": hit["_id"],
                    "source": hit["_source"],
                    "score": hit["_score"],
                    "highlight": hit.get("highlight", {})
                }
                for hit in data
            ]
            event = st.dataframe(
                data,
                column_config={
                    "source": {"json": True},
                    "highlight": {"json": True},
                },
                key="dataframe",
                on_select="rerun",
                selection_mode=["single-row", "single-column"],
            )

            if event and event["selection"]["rows"].__len__() > 0 and get_session_state("tab") == "explore":
                selected_data = data[event["selection"]["rows"][0]]
                data_visualizer_dialog(selected_data)
                


        else:
            st.write("No data found for the selected index.")
