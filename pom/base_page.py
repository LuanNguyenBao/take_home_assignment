from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


WAIT_TIMEOUT_SECONDS = 30


class BasePage:
    driver = None

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, WAIT_TIMEOUT_SECONDS)
        self.driver.maximize_window()

    def type_text(self, tuple_selector, value, timeout=WAIT_TIMEOUT_SECONDS):
        elem = self.wait_for_visibility_of_element_located(tuple_selector, timeout)
        elem.send_keys(value)

    def clear_and_type_text(self, tuple_selector, value, clear_by_keyboard=False):
        ele = self.wait_for_visibility_of_element_located(tuple_selector)
        self.click_element(tuple_selector)
        if clear_by_keyboard:
            ele.send_keys(Keys.CONTROL + "a")
            ele.send_keys(Keys.DELETE)
        else:
            ele.clear()
        self.wait_for_text_to_be_present(tuple_selector, '')
        ele.send_keys(value)

    def send_key(self, tuple_selector, tab=False, enter=False):
        ele = self.wait_for_visibility_of_element_located(tuple_selector)
        if tab:
            ele.send_keys(Keys.TAB)
        if enter:
            ele.send_keys(Keys.ENTER)

    def get_element_text(self, tuple_selector, timeout=WAIT_TIMEOUT_SECONDS):
        element = self.wait_for_visibility_of_element_located(tuple_selector, timeout)
        return element.text

    def click_element(self, tuple_selector, move_to_element=False, move_to_element_by_script=False,
                      timeout=WAIT_TIMEOUT_SECONDS, by_script=False):
        if move_to_element:
            self.move_to_element(tuple_selector, by_script=move_to_element_by_script)
        # Click element by webdriver or javascript
        if by_script:
            ele = self.wait_for_element_to_be_clickable(tuple_selector, timeout)
            self.driver.execute_script("arguments[0].click();", ele)
            self.driver.execute_script("return arguments[0].style", ele)
        else:
            ele = self.wait_for_element_to_be_clickable(tuple_selector, timeout)
            ele.click()

    def move_to_element(self, tuple_selector, by_script=False):
        ele = self.wait_element_exist(tuple_selector)
        if by_script:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", ele)
        else:
            actions = ActionChains(self.driver)
            actions.move_to_element(ele)
            actions.perform()

    def wait_for_text_to_be_present(self, tuple_selector, text, timeout=WAIT_TIMEOUT_SECONDS):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.text_to_be_present_in_element(tuple_selector, text))

    def wait_element_exist(self, tuple_selector, timeout=WAIT_TIMEOUT_SECONDS):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(tuple_selector))

    def wait_element_not_exist(self, tuple_selector, timeout=WAIT_TIMEOUT_SECONDS):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until_not(EC.presence_of_element_located(tuple_selector))

    def wait_for_visibility_of_element_located(self, tuple_selector, timeout=WAIT_TIMEOUT_SECONDS):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(tuple_selector))

    def wait_for_invisibility_of_element_located(self, tuple_selector, timeout=WAIT_TIMEOUT_SECONDS):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.invisibility_of_element_located(tuple_selector))

    def wait_for_element_to_be_clickable(self, tuple_selector, timeout=WAIT_TIMEOUT_SECONDS):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(tuple_selector))
    
    def find_elements(self, tuple_selector, timeout=WAIT_TIMEOUT_SECONDS):
        wait = WebDriverWait(self.driver, timeout)
        element_list = wait.until(EC.presence_of_all_elements_located(tuple_selector))
        return element_list

    @staticmethod
    def get_text_list(list_data):
        name_list = []
        for item in list_data:
            name_list.append(item.text)
        return name_list

    def get_text_of_elements(self, tuple_selector, move_to_element=False, timeout=WAIT_TIMEOUT_SECONDS):
        elements = self.find_elements(tuple_selector, timeout)
        if not move_to_element:
            return self.get_text_list(elements)
        text_list = []
        for e in elements:
            ActionChains(self.driver).move_to_element(e).perform()
            text_list.append(str(e.text))
        return text_list

    def get_attribute_of_element(self, tuple_selector, attribute, timeout=WAIT_TIMEOUT_SECONDS,
                                 move_to_element=False):
        if move_to_element:
            self.move_to_element(tuple_selector)
        element = self.wait_element_exist(tuple_selector, timeout)
        return element.get_attribute(attribute)

    def is_element_visible(self, tuple_selector, timeout=WAIT_TIMEOUT_SECONDS):
        try:
            self.wait_for_visibility_of_element_located(tuple_selector, timeout)
            return True
        except TimeoutException:
            return False

    def is_element_invisible(self, tuple_selector, timeout=WAIT_TIMEOUT_SECONDS):
        try:
            self.wait_for_invisibility_of_element_located(tuple_selector, timeout)
            return True
        except TimeoutException:
            return False

    def is_element_exist(self, tuple_selector, timeout=WAIT_TIMEOUT_SECONDS):
        try:
            self.wait_element_exist(tuple_selector, timeout)
            return True
        except TimeoutException:
            return False

    def is_element_not_exist(self, tuple_selector, timeout=WAIT_TIMEOUT_SECONDS):
        try:
            self.wait_element_not_exist(tuple_selector, timeout)
            return True
        except TimeoutException:
            return False
    
    def is_element_disable(self, tuple_selector):
        is_disabled = self.get_attribute_of_element(tuple_selector, 'disabled')
        if is_disabled is None:
            return False
        else:
            return True
