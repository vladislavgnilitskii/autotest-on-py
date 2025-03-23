import pytest
from fixture.application import Application

@pytest.fixture(scope= "session") #Инициализация фикстуры
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy) #Указание на то, как эта фикстура должна разрушаться
    return fixture