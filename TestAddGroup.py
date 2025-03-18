# -*- coding: utf-8 -*-
import pytest
from application import Application
from group import Group
#Файл, где при помощи вспомогательных функций делают тесты
@pytest.fixture #Инициализация фикстуры
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy) #Указание на то, как эта фикстура должна разрушаться
    return fixture

def test_add_group(app): #Тестовый метод
    app.login("admin", "secret")
    app.create_group(Group("House", "asl", "da"))
    app.logout()

def test_add_empty_group(app):
    app.login("admin", "secret")
    app.create_group(Group("", "", ""))
    app.logout()

