from playwright.sync_api import Page, expect
from src.ui.types.price_filtering_types import ProductFilterOptions

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.product_filter = page.locator('select[data-test="product-sort-container"]')
        self.item_prices = page.locator('.inventory_item_price')
        self.shopping_cart_badge = page.locator('[data-test="shopping-cart-badge"]')
        self.shopping_cart_button = page.locator('[data-test="shopping-cart-link"]')
        self.add_to_cart_buttons = {
            'sauce-labs-onesie': page.locator('[data-test="add-to-cart-sauce-labs-onesie"]'),
            'sauce-labs-bike-light': page.locator('[data-test="add-to-cart-sauce-labs-bike-light"]')
        }

    def filter_products(self, filter: ProductFilterOptions):
        self.product_filter.click()
        self.product_filter.select_option(label=filter.value)
        self.page.wait_for_load_state('networkidle')

    def get_item_prices(self) -> list[float]:
        self.item_prices.first.wait_for(state='visible')
        price_texts = self.item_prices.all_text_contents()
        return [float(price.replace('$', '')) for price in price_texts]

    def add_item_to_cart(self, item: str):
        self.add_to_cart_buttons[item].click()

    def get_shopping_cart_count(self) -> int:
        try:
            cart_count_text = self.shopping_cart_badge.text_content()
            return int(cart_count_text) if cart_count_text else 0
        except:
            return 0