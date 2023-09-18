#!/bin/bash

set -e

function check_requirements() {
  if [[ -z "$(command -v python3)" ]]; then
    echo "Please install 'python3' before running this script"
    exit 1
  fi
}

function main() {
  check_requirements

  [[ -z "$(command -v virtualenv)" ]] && \
    pip3 install virtualenv

  test -d .venv || virtualenv .venv
  source ".venv/bin/activate"

  pip3 install --upgrade pip

  python3 -m pip install --no-cache -r requirements.txt
}

main