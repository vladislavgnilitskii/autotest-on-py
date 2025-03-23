import pytest
from fixture.application import Application

fixture = None

@pytest.fixture #Инициализация фикстуры
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
        fixture.session.login("admin", "secret")
    else:
        if not fixture.is_valid():
            fixture = Application()
            fixture.session.login("admin", "secret")
    return fixture

@pytest.fixture(scope="session", autouse=True)  # Инициализация фикстуры
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin) #Указание на то, как эта фикстура должна разрушаться
    return fixture