import pytest
from features.test_base import TestBase
from pom.landing_page import LandingPage
from pom.search_result_page import SearchResultPage


@pytest.mark.search_city
class TestSearchCity(TestBase):

    def setup(self):
        self.landing_page = LandingPage(self.driver)
        self.search_result_page = SearchResultPage(self.driver)

    def test_search_weather_in_your_city(self):
        self.landing_page.open_landing_page()
        self.landing_page.wait_page_load()
        self.landing_page.perform_search_city_txt("Ho Chi Minh city")
        self.search_result_page.verify_first_search_result_title_lbl_is_displayed_as_expected("Thanh pho Ho Chi Minh, VN")
