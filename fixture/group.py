from selenium.webdriver.common.by import By

class GroupHelper:
    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        self.open_page()
        # init group creation
        wd.find_element(By.NAME, "new").click()
        # fill group firm
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
        # submit group creations
        wd.find_element(By.NAME, "submit").click()

    def open_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "groups").click()