
from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
import pytest
from selenium import webdriver
from utilities.fakeData import generate_fake_data
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os


class Test_001_AccountReg:
    logger = LogGen.loggen()
    baseURL = "http://demo.opencart.com/"

    def test_account_reg(self, setup):

        self.logger.info('started....................')
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.logger.info('launching app....................')
        try:
            self.hp = HomePage(self.driver)
            self.logger.info('clicking my_account....................')
            self.hp.clickMyAccount()
            self.logger.info('clicking Register....................')
            self.hp.clickRegister()

            self.logger.info('Providing customer details for registration....................')
            self.regpage = AccountRegistrationPage(self.driver)
            fake_data = generate_fake_data()
            self.regpage.setFirstName(fake_data["first_name"])
            self.regpage.setLastName(fake_data["last_name"])
            self.regpage.setEmail(fake_data["email"])
            self.regpage.setPassword(fake_data["password"])
            self.regpage.setPrivacyPolicy()
            self.regpage.clickContinue()

            wait = WebDriverWait(self.driver, 10)
            if wait.until(EC.title_is("Register Account")):
                self.logger.info('Account Registration Passed....................')
                assert True
                self.driver.close()
            else:
                self.driver.save_screenshot(os.path.abspath(os.curdir + '\\screenshots\\reg1.png'))
                self.logger.error('Account Registration failed....................')
                assert False
                self.driver.close()
            self.logger.info('completed....................')

        except Exception as e:
            self.driver.save_screenshot(os.path.abspath(os.curdir + '\\screenshots\\reg1.png'))
            self.logger.error(e)
            assert False

