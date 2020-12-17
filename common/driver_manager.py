from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from common.config_loader import EnvConf


class DriverManager(object):
    driver_dict = {}

    @staticmethod
    def init_driver(browser_name=None):
        if browser_name is None:
            browser_name = EnvConf.UI_BROWSER
        driver = None
        if browser_name == "chrome":
            options = ChromeOptions()
            options.add_experimental_option("excludeSwitches", ["enable-automation", 'enable-logging'])
            options.add_experimental_option('useAutomationExtension', False)
            options.add_experimental_option('prefs', {'credentials_enable_service': False,
                                                      'profile': {'password_manager_enabled': False}})
            driver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())

        if browser_name == "firefox":
            options = FirefoxOptions()
            options.add_argument("--enable-javascript")
            firefox_cap = webdriver.DesiredCapabilities.FIREFOX
            firefox_cap['marionette'] = True
            driver = webdriver.Firefox(options=options, executable_path=GeckoDriverManager().install(),
                                       capabilities=firefox_cap)

        if "edge" in browser_name:
            options = EdgeOptions()
            options.use_chromium = True
            driver = webdriver.Edge(capabilities=options.to_capabilities(),
                                    executable_path=EdgeChromiumDriverManager().install())

        driver.set_page_load_timeout(15)
        return driver
