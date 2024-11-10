import requests


def log_request(func):
    def wrapper(*args, **kwargs):
        print(f"Requesting {func.__name__} with args: {args} and kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

class OpenSearch():

    def __init__(self, endpoint: str, username: str, password: str):
        self.endpoint = endpoint
        self.username = username
        self.password = password

    def _GET(self, url: str):
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        return requests.get(url, auth=(self.username, self.password), headers=headers)

    def _PUT(self, url: str, data: dict):
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        return requests.put(url, auth=(self.username, self.password), headers=headers, json=data)

    def _POST(self, url: str, data: dict):
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        return requests.post(url, auth=(self.username, self.password), headers=headers, json=data)

    def _DELETE(self, url: str):
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        return requests.delete(url, auth=(self.username, self.password), headers=headers)

    def test_connection(self):
        response = self._GET(self.endpoint)
        return response.json()
    
    
    def get_all_indices(self):
        response = self._GET(f"{self.endpoint}/_cat/indices")
        return response.json()
    
    def get_index_info(self, index_name: str):
        response = self._GET(f"{self.endpoint}/{index_name}")
        return response.json()
    
    @log_request
    def edit_index_mapping(self, index_name: str, mapping: dict):
        response = self._PUT(f"{self.endpoint}/{index_name}/_mapping", mapping)
        print(f"Edit Index Mapping Response: {response.json()}")
        return response.json()
    
    @log_request
    def clone_index(self, source_index: str, target_index: str):
        data = {
            "source": {
                "index": source_index
            },
            "dest": {
                "index": target_index
            }
        }
        response = self._POST(f"{self.endpoint}/_reindex", data)
        print(f"Clone Index Response: {response.json()}")
        return response.json()

    def delete_index(self, index_name: str):
        response = self._DELETE(f"{self.endpoint}/{index_name}")
        print(f"Delete Index Response: {response.json()}")
        return response.json()

    def search_index(self, index_name: str):
        response = self._GET(f"{self.endpoint}/{index_name}/_search")
        return response.json()
        
client = None

def OpenSearchClient(endpoint: str, username: str, password: str):
    global client

    if client is None:
        client = OpenSearch(endpoint, username, password)
    return client

    