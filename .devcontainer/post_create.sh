#!/bin/bash

set -euo pipefail

curl https://install.duckdb.org | sh

DUCKDB=/home/vscode/.duckdb/cli/latest

echo "export PATH=${DUCKDB}:$PATH" >> ~/.bashrc
