import pytest
from common.driver_manager import DriverManager


driver = None


@pytest.fixture(scope="class")
def setup_driver(request):
    global driver
    driver = DriverManager.init_driver()
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            extra.append(pytest_html.extras.html('<div>Additional HTML If False UI Test</div>'))
            extra.append(pytest_html.extras.image(driver.get_screenshot_as_base64()))
            report.extra = extra
