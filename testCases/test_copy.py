from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
import time
import pytest
from selenium import webdriver
from utilities.fakeData import generate_fake_data
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import os
from selenium.webdriver.common.by import By




class Test_001_AccountReg:

    baseURL = "http://demo.opencart.com/"
    # baseURL = ReadConfig.getApplicationURL()

    def test_account_reg(self,setup):
        logger = LogGen.loggen()
        logger.info('starts...........')
        self.driver = setup

        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        # time.sleep(10)
        # self.driver.find_element(By.XPATH, '//*[@class="mark"]').click()
        # time.sleep(10)
        print("started ")

        self.hp = HomePage(self.driver)

        time.sleep(3)
        self.hp.clickMyAccount()
        time.sleep(3)
        self.hp.clickRegister()
        time.sleep(3)
        print("filling registration Page form")


        self.regpage = AccountRegistrationPage(self.driver)

        fake_data = generate_fake_data()
        self.regpage.setFirstName(fake_data["first_name"])
        self.regpage.setLastName(fake_data["last_name"])
        self.regpage.setEmail(fake_data["email"])
        self.regpage.setPassword(fake_data["password"])
        time.sleep(2)

        self.regpage.setPrivacyPolicy()
        self.regpage.clickContinue()
        print("registration succesfull")


        if self.driver.title == "Register Account":
            time.sleep(2)
            # self.driver.save_screenshot(os.path.abspath(os.curdir + '\\screenshots\\reg1.png'))
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir + '\\screenshots\\reg1.png'))
            assert False