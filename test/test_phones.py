import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.all_phones_from_view_page == merge_phones_like_on_view_page(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: emptycheck(x),
                            map(lambda x: clear(x),
                                    [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone])))


def merge_phones_like_on_view_page(contact):
    fst = None
    snd = None
    thrd = None
    frth = None
    fth = None
    if emptycheck(contact.firstname) and emptycheck(contact.lastname):
        fst = contact.firstname + " " + contact.lastname + "\n"
        sxth = "\n" + contact.firstname + "." + contact.lastname + "@"
        if emptycheck(contact.secondaryphone):
            fth = "P: " + contact.secondaryphone
    if emptycheck(contact.homephone):
        snd = "H: " + contact.homephone
    if emptycheck(contact.mobilephone):
        thrd = "M: " + contact.mobilephone
    if emptycheck(contact.workphone):
        frth = "W: " + contact.workphone

    return "\n".join(filter(lambda x: emptycheck(x), [fst, snd, thrd, frth, fth, sxth]))


def emptycheck(element):
    return element != "" and element is not None
