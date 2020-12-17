from selenium.webdriver.common.by import By
from pom.base_page import BasePage
from common.config_loader import EnvConf


loading_div = (By.CSS_SELECTOR, 'div.owm-loader')
search_city_txt = (By.CSS_SELECTOR, 'form[role="search"] > input[type="text"]')


class LandingPage(BasePage):

    def open_landing_page(self):
        self.driver.get(EnvConf.OPEN_WEATHER_URL)

    def wait_page_load(self):
        self.wait_for_invisibility_of_element_located(loading_div)

    def input_search_city_txt(self, value_city_input):
        self.type_text(search_city_txt, value=value_city_input)

    def perform_search_city_txt(self, value_city_input):
        self.input_search_city_txt(value_city_input)
        self.send_key(search_city_txt, enter=True)
