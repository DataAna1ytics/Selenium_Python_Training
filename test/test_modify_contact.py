from model.contact import Contact


def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(Contact("ftest", "mtest", "ltest", "ntest"))
    app.contact.modify_first_contact(Contact(firstname="New name"))


#def test_modify_contact_lastname(app):
#    if app.contact.count() == 0:
 #       app.contact.create(Contact("ftest", "mtest", "ltest", "ntest")))
#    app.contact.modify_first_contact(Contact(name="New last name"))
