# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_new_contact(Contact("fst", "mdl", "lst", "nck"))
    app.session.logout()
