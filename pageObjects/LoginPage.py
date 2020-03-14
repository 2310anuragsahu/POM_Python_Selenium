class LoginPageClass():

    # Locators
    textbox_username_id = "Email"
    text_password_id = "Password"
    login_button = "*//input[@type='submit']"
    link_logoutlinktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.text_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.login_button).click()

    def clickLogout(self):
        self.driver.find_element_by_xpath(self.link_logoutlinktext).click()
