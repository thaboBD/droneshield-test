import pytest
from playwright.sync_api import Page, expect
from src.ui.page_object_models.login_page import LoginPage
from src.ui.page_object_models.inventory_page import InventoryPage, ProductFilterOptions
from src.ui.page_object_models.checkout_page import CheckoutPage

@pytest.fixture(autouse=True)
def before_each_test(page: Page, base_url: str):
    page.goto(base_url)
    login_page = LoginPage(page)
    login_page.login('standard_user', 'secret_sauce')
    # Wait for the inventory page to load
    page.wait_for_selector('.inventory_list')
    yield page
    
@pytest.mark.ui
def test_product_filtering_price_low_to_high(page: Page, base_url: str):
    inventory_page = InventoryPage(page)
    
    expect(page).to_have_url(f'{base_url}inventory.html')
    
    initial_prices = inventory_page.get_item_prices()
    print(f"Initial prices: {initial_prices}")
    
    inventory_page.filter_products(ProductFilterOptions.PRICE_LOW_TO_HIGH)
    
    filtered_prices = inventory_page.get_item_prices()
    print(f"Filtered prices: {filtered_prices}")
    
    assert filtered_prices == sorted(filtered_prices), f"Prices are not sorted from low to high. Actual prices: {filtered_prices}"


@pytest.mark.ui
def test_e2e_purchase_flow(page: Page, base_url: str):
    inventory_page = InventoryPage(page)
    checkout_page = CheckoutPage(page)
    
    # Add items to cart
    inventory_page.add_item_to_cart('sauce-labs-onesie')
    cart_count = inventory_page.get_shopping_cart_count()
    assert cart_count == 1
    
    inventory_page.add_item_to_cart('sauce-labs-bike-light')
    cart_count = inventory_page.get_shopping_cart_count()
    assert cart_count == 2
    
    # Go to cart
    inventory_page.shopping_cart_button.click()
    page.wait_for_url('**/cart.html')
    expect(page).to_have_url(f"{base_url}cart.html")
    expect(page.get_by_text('Your Cart')).to_be_visible()
    expect(page.get_by_text('Sauce Labs Onesie')).to_be_visible()
    expect(page.get_by_text('Sauce Labs Bike Light')).to_be_visible()
    
    # Proceed to checkout
    checkout_page.checkout_button.click()
    expect(page).to_have_url(f"{base_url}checkout-step-one.html")
    
    # Enter customer information
    checkout_page.enter_customer_information('John', 'Doe', '1234')
    
    # Verify checkout overview
    expect(page.get_by_text('Checkout: Overview')).to_be_visible()
    expect(page.get_by_text('Sauce Labs Onesie')).to_be_visible()
    expect(page.get_by_text('Sauce Labs Bike Light')).to_be_visible()
    
    # Complete purchase
    checkout_page.finish_button.click()
    expect(page).to_have_url(f"{base_url}checkout-complete.html")
    expect(page.get_by_text('Checkout: Complete!')).to_be_visible()
    expect(page.get_by_text('Thank you for your order!')).to_be_visible()