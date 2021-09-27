from appium.webdriver.common.mobileby import MobileBy
from pages.base_page import BasePage
from pages.locators import MenuDrawer
from utils.logs.testlogger import Logger, info, error


logger = Logger().get_logger()


class MenuDrawerPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.all_lists = MenuDrawer.LIST_CONTAINER
        self.default_list = MenuDrawer.DEFAULT_LIST
        self.create_new = MenuDrawer.CREATE_NEW_LIST

    def get_all_lists_names(self):
        try:
            menu_children = self.all_lists.get_all_child_elements(MobileBy.CLASS_NAME, 'XCUIElementTypeCell')
            return [item.get_attribute('value') for item in menu_children]
        except AssertionError:
            error(logger, 'unable to locate list names within task menu')

    def select_item(self, title):
        try:
            menu_children = self.all_lists.get_all_child_elements(MobileBy.CLASS_NAME, 'XCUIElementTypeCell')
            for child in menu_children:
                if child.get_attribute('value') == title:
                    info(logger, f"selecting '{title}' from menu drawer")
                    child.click()
                    break
        except AssertionError:
            error(logger, 'unable to select item from menu drawer')
            pass

    def select_create_new_list(self):
        try:
            self.create_new.click()
            info(logger, 'clicked "create new list" from menu drawer')
        except AssertionError:
            error(logger, 'unable to click "create new list" from menu drawer')
            pass