from playwright.sync_api import Page, expect

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_button = page.get_by_role('button', name='Checkout')
        self.customer_first_name = page.locator('[data-test="firstName"]')
        self.customer_last_name = page.locator('[data-test="lastName"]')
        self.customer_postal_code = page.locator('[data-test="postalCode"]')
        self.finish_button = page.get_by_role('button', name='Finish')
        self.submit_customer_information_button = page.get_by_role('button', name='Continue')

    def enter_customer_information(self, first_name: str, last_name: str, postal_code: str):
        self.customer_first_name.fill(first_name)
        self.customer_last_name.fill(last_name)
        self.customer_postal_code.fill(postal_code)
        self.submit_customer_information_button.click()
