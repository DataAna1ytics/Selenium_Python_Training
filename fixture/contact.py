import time
class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
        # return to groups page
        driver = self.app.driver
        driver.find_element_by_link_text("home").click()

    def add_new_contact(self, contact):
        # add new contact
        driver = self.app.driver
        driver.find_element_by_link_text("add new").click()
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys(contact.firstname)
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys(contact.middlename)
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys(contact.lastname)
        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("nickname").send_keys(contact.nickname)
        driver.find_element_by_name("submit").click()

    def delete_first_contact(self):
        driver = self.app.driver
        # select first contact
        driver.find_element_by_name("selected[]").click()
        # submit deletion
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Select all'])[1]/following::input[2]").click()
        driver.switch_to_alert().accept()
        time.sleep(5)
        self.return_to_home_page()

    def modify_first_contact(self):
        driver = self.app.driver
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='ftest.ltestmtest.@'])[1]/following::img[2]").click()
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys("0000")
        driver.find_element_by_name("update").click()
        driver.find_element_by_link_text("home page").click()
