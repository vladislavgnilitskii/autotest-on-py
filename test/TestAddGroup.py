# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.group import Group
#Файл, где при помощи вспомогательных функций делают тесты
@pytest.fixture #Инициализация фикстуры
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy) #Указание на то, как эта фикстура должна разрушаться
    return fixture

def test_add_group(app): #Тестовый метод
    app.session.login("admin", "secret")
    app.create_group(Group("House", "asl", "da"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login("admin", "secret")
    app.create_group(Group("", "", ""))
    app.session.logout()

