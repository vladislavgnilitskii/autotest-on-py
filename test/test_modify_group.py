from model.group import Group

def test_modify_group_name(app): #Тестовый метод
    if app.group.count() == 0:
        app.group.create(Group(name=""))
    app.group.modify_first_group(Group(name="New group"))

def test_modify_group_header(app): #Тестовый метод
    if app.group.count() == 0:
        app.group.create(Group(header=""))
    app.group.modify_first_group(Group(header="New header"))