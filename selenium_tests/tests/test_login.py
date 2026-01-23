import pytest
from selenium_tests.pages.login_page import LoginPage
from selenium_tests.utils.driver_factory import get_driver

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

@pytest.mark.smoke
def test_valid_login(driver):
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    assert "inventory" in driver.current_url
