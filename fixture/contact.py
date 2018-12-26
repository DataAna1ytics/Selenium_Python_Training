class ContactHelper:

    def __init__(self, app):
        self.app = app

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
