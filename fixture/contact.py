import time


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
        # return to groups page
        driver = self.app.driver
        if not driver.current_url.endswith("/addressbook/"):
            driver.find_element_by_link_text("home").click()

    def add_new_contact(self, contact):
        # add new contact
        driver = self.app.driver
        driver.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        driver.find_element_by_name("submit").click()

    def fill_contact_form(self, contact):
        driver = self.app.driver
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)

    def change_field_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self):
        driver = self.app.driver
        # select first contact
        self.select_first_contact()
        # submit deletion
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Select all'])[1]/following::input[2]").click()
        driver.switch_to_alert().accept()
        time.sleep(5)
        self.return_to_home_page()

    def modify_first_contact(self, new_contact_data):
        driver = self.app.driver
        # open modification form
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='ftest.ltestmtest.@'])[1]/following::img[2]").click()
        # fill group form
        self.fill_contact_form(new_contact_data)
        # submit modification
        driver.find_element_by_name("update").click()
        driver.find_element_by_link_text("home page").click()

    def select_first_contact(self):
        driver = self.app.driver
        driver.find_element_by_name("selected[]").click()

    def count(self):
        driver = self.app.driver
        self.return_to_home_page()
        return len(driver.find_elements_by_name("selected[]"))
