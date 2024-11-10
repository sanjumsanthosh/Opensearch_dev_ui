# opensearch-dev-ui

## Project Description

`opensearch-dev-ui` is a Streamlit-based user interface for interacting with OpenSearch. It provides various tabs for configuration, indexing, exploring, and adding records to OpenSearch.

## Features

- **Configuration Tab**: Configure settings for OpenSearch.
- **Index Tab**: Manage and view indices in OpenSearch.
- **Explore Tab**: Explore and query data in OpenSearch.
- **Record Add Tab**: Add new records to OpenSearch.

## Prerequisites

- Docker
- Docker Compose
- Python 3.8 or higher

## Setup Instructions

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/opensearch-dev-ui.git
    cd opensearch-dev-ui
    ```

2. **Build and start the Docker containers**:
    ```sh
    docker-compose up --build
    ```

3. **Install Python dependencies**:
    ```sh
    pip install -r requirements.lock
    ```

4. **Run the application**:
    ```sh
    streamlit run src/opensearch_dev_ui/app.py
    ```

## Usage

Once the application is running, open your web browser and navigate to `http://localhost:8501`. You will see the following tabs:

- **Configuration**: Configure settings for OpenSearch.
- **Index**: Manage and view indices in OpenSearch.
- **Explore**: Explore and query data in OpenSearch.
- **Record Add**: Add new records to OpenSearch.

## Development

To set up the development environment, follow these steps:

1. **Install development dependencies**:
    ```sh
    rye sync
    ```

2. **Run the application in development mode**:
    ```sh
    rye run dev
    ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
