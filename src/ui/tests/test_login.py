import pytest
from playwright.sync_api import Page, expect
from src.ui.page_object_models.login_page import LoginPage

@pytest.fixture(autouse=True)
def before_each_test(page: Page, base_url: str):
    page.goto(base_url)
    expect(page).to_have_title('Swag Labs')
    yield  

@pytest.mark.ui
def test_login_to_swag_labs_successfully(page: Page, base_url: str):
    login_page = LoginPage(page)
    
    login_page.login('standard_user', 'secret_sauce')
    
    products_header = page.get_by_text('Products')
    expect(products_header).to_be_visible(timeout=10000)
    
    expect(page).to_have_url(f'{base_url}inventory.html')
    expect(page.get_by_text('Sauce Labs Backpack')).to_be_visible()

@pytest.mark.ui
def test_login_to_swag_labs_with_invalid_credentials(page: Page, base_url: str):
    login_page = LoginPage(page)
    
    login_page.login('locked_out_user', 'secret_sauce')
    
    error_message = page.get_by_text('Epic sadface: Sorry, this user has been locked out.')
    expect(error_message).to_be_visible(timeout=10000)
    
    expect(page).to_have_url(f'{base_url}')
    expect(page.get_by_text('Username')).to_be_visible()
    expect(page.get_by_text('Password')).to_be_visible()
    expect(page.get_by_text('Login')).to_be_visible()
    expect(page.get_by_text('Epic sadface: Sorry, this user has been locked out.')).to_be_visible()