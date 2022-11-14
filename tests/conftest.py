import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="function")
def driver():
    driver_service = Service(executable_path="D:/Project/SKILLFACTORY/U28_Rostelecom/chromedriver.exe")
    driver = webdriver.Chrome(service=driver_service)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver