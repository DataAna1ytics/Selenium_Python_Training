class SessionHelper:
    def __init__(self, app):
        self.app = app

    def logout(self):
        # logout
        driver = self.app.driver
        driver.find_element_by_link_text("Logout").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")

    def login(self, username, password):
        # login
        driver = self.app.driver
        self.app.open_home_page()
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
#        driver.find_element_by_id("LoginForm").click()
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Password:'])[1]/following::input[2]").click()

    def ensure_logout(self):
        driver = self.app.driver
        if self.is_logged_in() > 0:
            self.logout()

    def is_logged_in(self):
        driver = self.app.driver
        return len(driver.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, username):
        driver = self.app.driver
        return driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Address Book'])[1]/preceding::b[1]") \
               == "("+username+")"

    def ensure_login(self, username, password):
        driver = self.app.driver
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)
