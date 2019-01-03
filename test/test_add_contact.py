# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.add_new_contact(Contact("ftest", "mtest", "ltest", "ntest"))


def test_add_second_contact(app):
    app.contact.add_new_contact(Contact("sectest", "msectest", "lsectest", "nsectest"))
