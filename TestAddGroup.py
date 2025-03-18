# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

from application import Application
from group import Group

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_add_group(self):
        self.app.login("admin", "secret")
        self.app.create_group(Group("House", "asl", "da"))
        self.app.logout()

    def test_add_empty_group(self):
        self.app.login("admin", "secret")
        self.app.create_group(Group("", "", ""))
        self.app.logout()


    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to.alert
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):
        self.app.destroy()

if __name__ == "__main__":
    unittest.main()
