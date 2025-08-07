#!/bin/sh

export WEBDRIVER=$1
export PYTHONPATH=$(pwd)
export HEADLESS=$2

echo "Running tests with WebDriver: $WEBDRIVER"

if [ "$WEBDRIVER" == "chrome" ] || [ "$WEBDRIVER" == "firefox" ]; then
    pytest tests/
else
    echo "Invalid WebDriver specified. Please put chrome or firefox as the first argument"
fi