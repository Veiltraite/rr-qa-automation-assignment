# rr-qa-automation-assignment

Automated UI/API testing using Python and Pytest on [tmdb-discover](https://tmdb-discover.surge.sh/)

---

## Tech Stack
```
    Python 3.9+
    Pytest – Test framework
    Requests – For making API calls
    Selenium – Test automation tool for web applications
```

---

## Setup

1. **Install Python** *(if not already installed)*  
    Download and install Python 3.9+ from the [official Python website](https://www.python.org/downloads/).  
    *After installation, confirm with:*
    ```bash
    python --version
    ```

2. **Create a Virtual Environment (Recommended)**  
    ```bash
    python3 -m venv ~/venv
    ```
    *then, run this command below to activate the virtual environment*
    ```bash
    source ~/venv/bin/activate
    ```

3. **Clone the Repository**  
    ```bash
    git clone git@github.com:Veiltraite/rr-qa-automation-assignment.git
    ```

4. **Move to the project directory**  
    ```bash
    cd frr-qa-automation-assignment
    ```

5. **Install Dependencies**  
    ```bash
    pip install -r requirements.pip
    ```

---

## Run Tests

To execute the test, run command below:
*To use chrome:*
```
source execute_test.sh chrome
```
*To use firefox:*
```
source execute_test.sh firefox
```

---

## Project Structure
```
    rr-qa-automation-assignment/
    ├── src/
    │    ├── api
    │    │    ├── __init__.py     # Module interface to access API class
    │    │    ├── base.py         # Base API class that contains general configs, values, and API methods 
    │    │    └── tmdb_api.py     # Contains classes for making API request and get/processing response
    │    └── web
    │    │    ├── __init__.py     # Module interface to access Page class
    │    │    ├── base.py         # Base Page class that contains general configs, values, and element interaction methods 
    │    │    └── tmdb_page.py    # Contains classes for defining / processing elements and actions
    ├── tests/
    │    ├── conftest.py          # Config file to define fixtures for setup and teardown
    │    ├── pytest.ini           # Pytest config
    │    └── tmdb_test.py         # Main test cases
    ├── utils/
    │    └── driver.py           # Defining web driver to be used
    ├── execute_test.sh          # Shell script to execute tests
    ├── requirements.pip         # Dependencies
    └── README.md
```