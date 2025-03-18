# -*- coding: utf-8 -*-
from model.group import Group
#Файл, где при помощи вспомогательных функций делают тесты

def test_add_group(app): #Тестовый метод
    app.session.login("admin", "secret")
    app.group.create(Group("House", "asl", "da"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login("admin", "secret")
    app.group.create(Group("", "", ""))
    app.session.logout()

