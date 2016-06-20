#!/usr/bin/env bash
set -efu

SCRIPTS_DIR=$(dirname -- $0)
BASE_DIR=$(dirname -- "${SCRIPTS_DIR}")

. "${SCRIPTS_DIR}/_colours.sh"

echo_green "Bumping from version 1 to 2"
sed -i'' -e "s/VERSION = 1/VERSION = 2/" "${BASE_DIR}/src/mysite/settings.py"
echo_green "Bumped 'VERSION' setting to 2"
echo "Don't forget to run the following:"
echo_yellow "    docker build -t web:2 ."

