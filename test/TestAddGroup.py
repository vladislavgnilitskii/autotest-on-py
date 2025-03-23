# -*- coding: utf-8 -*-
from model.group import Group
#Файл, где при помощи вспомогательных функций делают тесты

def test_add_group(app): #Тестовый метод
    app.group.create(Group("House", "asl", "da"))

def test_add_empty_group(app):
    app.group.create(Group("", "", ""))

