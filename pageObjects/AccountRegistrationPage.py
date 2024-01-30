from selenium.webdriver.common.by import By
import time


class AccountRegistrationPage():

    first_name_xpath = '//*[@id="input-firstname"]'
    last_name_xpath = '//*[@id="input-lastname"]'
    email_xpath = '//*[@id="input-email"]'
    password_xpath = '//*[@id="input-password"]'
    chk_policy_xpath = '//*[@class="form-check-input" and @name = "agree"]'
    continue_btn_xpath = '//*[@class="btn btn-primary" and  contains(text(), "Continue")]'

    def __init__(self, driver):
        self.driver = driver

    def setFirstName(self,fname):
      self.driver.find_element(By.XPATH,self.first_name_xpath).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.XPATH,self.last_name_xpath).send_keys(lname)

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.email_xpath).send_keys(email)


    def setPassword(self,pwd):
        self.driver.find_element(By.XPATH,self.password_xpath).send_keys(pwd)


    def setPrivacyPolicy(self):
        agree_element = self.driver.find_element(By.XPATH, self.chk_policy_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", agree_element)
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.chk_policy_xpath).click()

    def clickContinue(self):
        self.driver.find_element(By.XPATH,self.continue_btn_xpath).click()

