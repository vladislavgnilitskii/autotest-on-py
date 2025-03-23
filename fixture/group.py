from selenium.webdriver.common.by import By

class GroupHelper:
    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element(By.NAME, "new").click()
        # fill group firm
        self.fill_group_form(group)
        # submit group creations
        wd.find_element(By.NAME, "submit").click()

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, filed_name, test):
        wd = self.app.wd
        if test is not None:
            wd.find_element(By.NAME, filed_name).click()
            wd.find_element(By.NAME, filed_name).clear()
            wd.find_element(By.NAME, filed_name).send_keys(test)

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        wd.find_element(By.NAME, "delete").click()
        wd.find_element(By.LINK_TEXT, "group page").click()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "selected[]").click()

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        wd.find_element(By.NAME, "edit").click()
        # изменяем только те поля, которые переданы в new_group_data
        self.change_fields_group("group_name", new_group_data.name)
        self.change_fields_group("group_header", new_group_data.header)
        self.change_fields_group("group_footer", new_group_data.footer)
        wd.find_element(By.NAME, "update").click()
        wd.find_element(By.LINK_TEXT, "group page").click()

    def change_fields_group(self, type_group, new_group_data):
        if new_group_data is not None:
            self.change_field_value(type_group, new_group_data)

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements(By.NAME, "new")) > 0):
            wd.find_element(By.LINK_TEXT, "groups").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements(By.NAME, "selected[]"))
