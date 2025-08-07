# rr-qa-automation-assignment

Automated UI/API testing using Python and Pytest on [tmdb-discover](https://tmdb-discover.surge.sh/)

---

## Tech Stacks
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

## CI/CD Integration
The CI/CD integration concept can be done by using Github Action

*CI integration:*
1. create new yml file under .github/workflows folder.
2. configure the run condition everytime there is PR review and new changes merged into master branch.
3. configure the job steps to run code format checker such as black / pylint
4. configure the next job steps by following the [Setup](https://github.com/Veiltraite/rr-qa-automation-assignment?tab=readme-ov-file#setup) and [Run Test](https://github.com/Veiltraite/rr-qa-automation-assignment?tab=readme-ov-file#run-tests) flow.
5. PR can be merged once all of the code format checker and test automation run are done


*The CD integration:*
1. on other project / repository, create new yml file under .github/workflows folder.
2. configure the run condition everytime there is changes being merged in branch that being used in testing environment.
3. would not recommend to run test automation on production / live environment, it might affecting user experience and tempering with real customer data.
4. configure the job steps by following the [Setup](https://github.com/Veiltraite/rr-qa-automation-assignment?tab=readme-ov-file#setup) and [Run Test](https://github.com/Veiltraite/rr-qa-automation-assignment?tab=readme-ov-file#run-tests) flow.
5. if the CI is being run in cloud server / docker environment, please set the driver to Headless.
6. would not recommend to set the test automation flow as dependencies to do deployment since it might takes time.