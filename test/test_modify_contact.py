from model.contact import Contact


def test_modify_contact_name(app):
    app.contact.modify_first_contact(Contact(firstname="New name"))


#def test_modify_contact_lastname(app):
#    app.contact.modify_first_contact(Contact(name="New last name"))
