import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


class Test_003_AddCustomer:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen() # Logger

    @pytest.mark.sanity
    def test_addCustomer(self,setup):

        self.logger.info("***Test_003_AddCustomer***")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("*** Login Successful ***")

        self.logger.info("*** Starting Add Customer Test ***")

        self.adcust = AddCustomer(self.driver)
        self.adcust.clickOnCustomersMenu()
        self.adcust.clickOnCustomersMenuItem()

        self.adcust.clickOnAddnew()

        self.logger.info("*** Providing Customer Info ***")

        self.email = random_generator() + "@gmail.com"
        self.adcust.setEmail(self.email)
        self.adcust.setPassword("test123")
        self.adcust.setFirstName("Karan")
        self.adcust.setLastName("Kothavale")
        self.adcust.setGender("Male")
        self.adcust.setDob("5/20/1998")
        self.adcust.setCompanyName("busyQA")
        self.adcust.setNewsletter()
        self.adcust.setCustomerRoles("Guests")
        self.adcust.setManagerOfVendor("Vendor 2")
        self.adcust.setAdminContent("This is for testing....")
        self.adcust.clickOnSave()

        self.logger.info("*** Saving customer info")

        self.logger.info("*** Add customer validation started ***")

        self.msg = self.driver.find_element_by_tag_name("body").text

        print(self.msg)

        if "The new customer has been added successfully." in self.msg:

            assert True == True
            self.logger.info("*** Add Customer Test Passed ***")

        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_src.png")
            self.logger.info("*** Add Customer Test Failed ***")
            assert True == False

        self.driver.close()
        self.logger.info("*** Ending Home Page Title Test ***")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):

    return ''.join(random.choice(chars) for x in range(size))











