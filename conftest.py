import pytest
from playwright.sync_api import Page, Browser, Playwright, APIRequestContext

def pytest_addoption(parser):
    parser.addini('ui_base_url', 'base url for UI tests')
    parser.addini('api_base_url', 'base url for API tests')

def pytest_configure(config):
    config.addinivalue_line("markers", "ui: mark test as ui test")
    config.addinivalue_line("markers", "api: mark test as api test")

@pytest.fixture(scope="session")
def browser(playwright: Playwright, browser_name: str) -> Browser:
    browser_type = getattr(playwright, browser_name)
    browser = browser_type.launch(headless=True)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def page(browser: Browser, request) -> Page:
    base_url = request.config.getini('ui_base_url')
    page = browser.new_page(base_url=base_url)
    yield page
    page.close()

@pytest.fixture(scope="session")
def api_base_url(request) -> str:
    base_url = request.config.getini('api_base_url')
    print(f"API Base URL from ini file: {base_url}")  # Add this line
    return base_url

@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright, api_base_url: str) -> APIRequestContext:
    request_context = playwright.request.new_context(base_url=api_base_url)
    yield request_context
    request_context.dispose()

@pytest.fixture(scope="function")
def api_request(api_request_context: APIRequestContext) -> APIRequestContext:
    return api_request_context