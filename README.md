# DroneShield Test Project

This project contains automated tests for API and UI. It uses pytest and Playwright for testing.

**Playwright was chosen as the framework because it is easy to setup, and east to manage the browsers. Playwrigh also has auto waiting and better handling of dyanmic content allowing for easier automation of UIs built in React, Angular, Vue with less boiler plate code being written**

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
