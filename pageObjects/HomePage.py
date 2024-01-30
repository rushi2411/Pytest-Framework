from selenium.webdriver.common.by import By


class HomePage:
    lnk_myaccount_xpath = '//*[@class="d-none d-md-inline" and contains(text(), "My Account")]'
    lnk_register_xpath = '//*[@class = "dropdown-item" and contains(text(),"Register" )]'
    lnk_login_xpath = '//*[@class = "dropdown-item" and contains(text(),"Login" )]'
    # /test
    def __init__(self, driver):
        self.driver = driver

    def clickMyAccount(self):
        self.driver.find_element(By.XPATH, self.lnk_myaccount_xpath).click()

    def clickRegister(self):
        self.driver.find_element(By.XPATH,self.lnk_register_xpath).click()

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.lnk_login_xpath).click()