
import sys
from streamlit.web import cli as stcli
from .opensearch.opensearch import OpenSearchClient
from .utils.streamitUtils import set_session_state, get_session_state

def main():
    sys.argv = ["streamlit", "run", "src/opensearch_dev_ui/app.py"]
    sys.exit(stcli.main())

if __name__ == "__main__":
    main()