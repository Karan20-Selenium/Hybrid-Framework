import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture()
def setup(browser):

    #browser = "chrome"

    if browser == "chrome" :

        driver = webdriver.Chrome(ChromeDriverManager().install())

    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    elif browser == "edge":
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())

    else:
        # print("Please pass the correct browser name : " +browserName)
        raise Exception("browser is not found")

    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.delete_all_cookies()

    return driver

def pytest_addoption(parser):    # This will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

############## pyTest HTML Report#####################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Karan'


# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)















