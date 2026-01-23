from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_driver():
    """
    Creates and returns a Chrome WebDriver instance.
    Centralized driver creation helps with scalability.
    """
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    return driver