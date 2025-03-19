from selenium.webdriver.common.by import By

class GroupHelper:
    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        self.open_page()
        # init group creation
        wd.find_element(By.NAME, "new").click()
        self.fill_group_form(group)
        # submit group creations
        wd.find_element(By.NAME, "submit").click()

    def fill_group_form(self, group):
        wd = self.app.wd
        wd.find_element(By.NAME, "group_name").click()
        wd.find_element(By.NAME, "group_name").clear()
        wd.find_element(By.NAME, "group_name").send_keys(group.name)
        wd.find_element(By.NAME, "group_header").click()
        wd.find_element(By.NAME, "group_header").clear()
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").click()
        wd.find_element(By.NAME, "group_footer").clear()
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        wd.find_element(By.ID, "container").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_page()
        self.select_first_group()
        wd.find_element(By.NAME, "delete").click()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "selected[]").click()

    def open_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "groups").click()

    def modify_first_group(self, new_group_date):
        wd = self.app.wd
        self.open_page()
        # open modification form
        wd.find_element(By.NAME, "edit").click()
        #fill group
        self.fill_group_form(new_group_date)
        #submit modification
        wd.find_element(By.NAME, "update").click()
