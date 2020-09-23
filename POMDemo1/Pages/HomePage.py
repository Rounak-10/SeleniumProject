class HomePage():

    def __init__(self,driver):
        self.driver = driver

        self.click_on_welcome = "welcome"
        self.click_on_logout = "Logout"

    def ClickWelcome(self):
        self.driver.find_element_by_id(self.click_on_welcome).click()

    def ClickLogout(self):
        self.driver.find_element_by_link_text(self.click_on_logout).click()
