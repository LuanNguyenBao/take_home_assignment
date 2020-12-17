from selenium.webdriver.common.by import By
from assertpy import assert_that
from pom.base_page import BasePage


first_search_result_title_lbl = (By.CSS_SELECTOR, 'table tr:nth-child(1) > td:nth-child(2) > b:nth-child(1) > a')


class SearchResultPage(BasePage):

    def get_text_first_search_result_title_lbl(self):
        return self.get_element_text(first_search_result_title_lbl)

    def verify_first_search_result_title_lbl_is_displayed_as_expected(self, expected_value):
        assert_that(self.get_text_first_search_result_title_lbl(),
                    description="The first search result title label not display as expected").is_equal_to(expected_value)
