# DroneShield Test Project

This project contains automated tests for API and UI. It uses pytest and Playwright for testing.

**Playwright was selected as the framework due to its ease of setup and browser management. Its automatic waiting and handling of dynamic content make it ideal for automating UIs built with React, Angular, or Vue. This reduces the need for boilerplate code and simplifies the automation process.**

## Prerequisites

- Python 3.10 or higher
- pip (Python package installer)
- venv installed 
for mac/linux ```  python3 -m pip install venv```
for windows ```  python -m pip install venv```

## Setup

1. Clone the repository:
```git clone https://github.com/thaboBD/droneshield-test.git```
```cd droneshield-test```
Copy
2. Create a virtual environment:
```python3 -m venv venv```
Copy
3. Activate the virtual environment:
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```
- On Windows:
  ```
  venv\Scripts\activate
  ```

4. Install the required packages:
pip install -r requirements.txt
Copy
5. Install Playwright browsers:
playwright install
Copy
## Running Tests

Make sure your virtual environment is activated before running tests.

- To run all tests:
```pytest```
- To run only API tests:
```pytest -m api```

- To run only UI tests:
  ```pytest -m ui```

- To run tests with detailed output:
```pytest -v```

## Deactivating the Virtual Environment

When you're done, you can deactivate the virtual environment:
```deactivate```

## Running tests in CI
The tests can be run using github workflows. currently the run is triggerred manually and ran in a Docker container.

- To run the test click on the actions tab in the Repo or navigate to https://github.com/thaboBD/droneshield-test/actions
- Select the Manual Test Execution workflow on the right
- Click run workflow and select whether you want to run the UI, API or both test suites
