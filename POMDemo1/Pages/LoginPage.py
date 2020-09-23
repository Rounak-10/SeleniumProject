from POMDemo.Locators.locators1 import Locators
class LoginPage():

    #Login Page Objects
    def __init__(self,driver):
        self.driver = driver

        self.Username_textbox_id = Locators.Username_textbox_id
        self.Password_textbox_id = Locators.Password_textbox_id
        self.LoginButton = Locators.LoginButton


    def enter_username(self,username):
        #self.driver.find_element_by_id(Locators.Username_textbox_id).clear()
        self.driver.find_element_by_id(Locators.Username_textbox_id).send_keys("Admin")

    def enter_password(self, password):
        #self.driver.find_element_by_id(self.Password_textbox_id).clear()
        self.driver.find_element_by_id(self.Password_textbox_id).send_keys("admin123")

    def enter_login(self):
        self.driver.find_element_by_id(self.LoginButton).click()

    #Home Page Objects