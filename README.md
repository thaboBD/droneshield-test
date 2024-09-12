# DroneShield Test Project

This project contains automated tests for the DroneShield API and UI. It uses pytest and Playwright for testing.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Setup

1. Clone the repository:
git clone https://github.com/your-username/droneshield-test.git
cd droneshield-test
Copy
2. Create a virtual environment:
python3 -m venv venv
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
pytest
Copy
- To run only API tests:
pytest -m api
Copy
- To run only UI tests:
pytest -m ui
Copy
- To run tests with detailed output:
pytest -v
Copy
## Deactivating the Virtual Environment

When you're done, you can deactivate the virtual environment:
deactivate
