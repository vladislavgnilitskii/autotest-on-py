

def test_delete_first_group(app): #Тестовый метод
    app.session.login("admin", "secret")
    app.group.delete_first_group()
    app.session.logout()
