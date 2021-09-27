from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from pages.base_page import BasePage
from pages.locators import TasksScreen
from utils.logs.testlogger import Logger, info, error

logger = Logger().get_logger()


class TaskListPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.list_scroll_menu = TasksScreen.LIST_SCROLL_MENU
        self.default_list_tab = TasksScreen.DEFAULT_LIST_TAB
        self.new_list_tab = TasksScreen.NEW_LIST_TAB
        self.empty_list = TasksScreen.EMPTY_LIST_TEXT
        self.item_container = TasksScreen.ITEM_CONTAINER

    def click_new_list(self):
        try:
            self.new_list_tab.click()
            info(logger, 'clicked new list tab')
        except AssertionError:
            error(logger, 'unable to click new list tab')
            pass

    def click_default_list(self):
        try:
            self.default_list_tab.click()
            info(logger, 'clicked default list tab')
        except AssertionError:
            error(logger, 'unable to click default list tab')
            pass

    def click_custom_list(self, list_name):
        try:
            menu_children = self.list_scroll_menu.get_all_child_elements(MobileBy.CLASS_NAME, 'XCUIElementTypeButton')
            for child in menu_children:
                if child.get_attribute('name') == list_name:
                    child.click()
                    break
        except AssertionError:
            error(logger, 'unable to click on list name from top scroll menu')

    def get_all_list_names(self):
        try:
            menu_children = self.list_scroll_menu.get_all_child_elements(MobileBy.CLASS_NAME, 'XCUIElementTypeButton')
            return [item.get_attribute('name') for item in menu_children]
        except AssertionError:
            error(logger, 'unable to locate list names within tasks menu')

    def verify_list_in_menu(self, list_name):
        menu_items = self.get_all_list_names()
        info(logger, f'found task scroll-menu items: {menu_items}')
        if isinstance(list_name, str):
            return list_name in menu_items
        elif isinstance(list_name, list):
            return all(name in menu_items for name in list_name)

    def get_active_menu_tab(self):
        menu_children = self.list_scroll_menu.get_all_child_elements(MobileBy.CLASS_NAME, 'XCUIElementTypeButton')
        for child in menu_children:
            if child.get_attribute('value') == "1":
                return child.get_attribute('name')

    def get_all_incomplete_item_titles(self):
        try:
            item_children = self.item_container.get_all_child_elements(MobileBy.CLASS_NAME, 'XCUIElementTypeButton')
            return [item.get_attribute('name') for item in item_children]
        except AssertionError:
            error(logger, 'unable to locate items within list screen')

    def expand_completed_list(self):
        task_items = self.item_container.get_all_child_elements(MobileBy.CLASS_NAME, 'XCUIElementTypeCell')
        for item in task_items:
            if item.get_attribute('name') is not None:
                item.click()

    def get_all_list_items(self):
        """generate a dictionary w/ items and counts"""
        items_dict = {"complete_count": 0, "complete_items": [], "incomplete_count": 0, "incomplete_items": []}
        try:
            self.expand_completed_list()
            all_items = self.item_container.get_all_child_elements(MobileBy.CLASS_NAME, 'XCUIElementTypeButton')
            all_item_titles = [item.get_attribute('name') for item in all_items]
            for title in all_item_titles:
                if "Not starred" in title:
                    items_dict["incomplete_count"] += 1
                    items_dict["incomplete_items"].append(title)
                else:
                    items_dict["complete_count"] += 1
                    items_dict["complete_items"].append(title)
            return items_dict
        except AssertionError:
            error(logger, 'unable to locate items within list screen')

    def select_item_status_radio_btn(self):
        actions = TouchAction(self.driver)
        actions.tap(None, 10, 170).perform()

    def select_task(self, task_title):
        try:
            item_children = self.item_container.get_all_child_elements(MobileBy.CLASS_NAME, 'XCUIElementTypeButton')
            for item in item_children:
                if task_title in item.get_attribute('name'):
                    item.click()
                    break
        except AssertionError:
            error(logger, 'unable to click on a task line item')

    def get_completed_task_count(self):
        """check the value displayed in the 'Completed' label"""
        try:
            task_items = self.driver.find_elements_by_class_name('XCUIElementTypeCell')
            for item in task_items:
                if item.get_attribute('name') is not None:
                    label = item.get_attribute('name')
                    return int(label[label.find("(") + 1:label.find(")")])
        except AssertionError:
            error(logger, 'unable to locate "Completed" label on task list screen')