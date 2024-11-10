#!/bin/bash
set -e

# Install the plugin
/usr/share/opensearch/bin/opensearch-plugin install --batch analysis-kuromoji

# Execute the original entrypoint
exec /usr/share/opensearch/opensearch-docker-entrypoint.sh "$@"