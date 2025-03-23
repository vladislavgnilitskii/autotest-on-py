from model.group import Group

def test_modify_group_name(app): #Тестовый метод
    app.group.modify_first_group(Group(name="New group"))

def test_modify_group_header(app): #Тестовый метод
    app.group.modify_first_group(Group(header="New header"))