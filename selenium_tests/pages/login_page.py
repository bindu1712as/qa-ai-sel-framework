from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    """
    Page Object representing the Login page.
    """

    def __init__(self, driver):
        self.driver = driver
        self.username = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.login_btn = (By.ID, "login-button")

    def login(self, user, pwd):
        """
        Perform login action.
        """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.username)
        ).send_keys(user)

        self.driver.find_element(*self.password).send_keys(pwd)
        self.driver.find_element(*self.login_btn).click()
