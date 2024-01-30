import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser=='edge':
        driver = webdriver.Edge()
        print('launching Edge browser...............')

    elif browser=='firefox':
        driver = webdriver.Firefox()
        print('launching Edge firefox...............')

    else:
        driver = webdriver.Chrome()
        print('launching Chrome browser...............')
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
