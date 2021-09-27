import inspect
from GLOBALS import *
from tests.base_test import BaseTest
from pages.page_tasks import TaskListPage
from pages.page_new_list import NewListPage
from pages.drawer_menu import MenuDrawerPage
from pages.drawer_options import OptionsDrawerPage
from delayed_assert import expect, assert_expectations
from utils.logs.testlogger import Logger, info

logger = Logger().get_logger()


class TestListActionsSuite(BaseTest):

    def test_default_list_tabs(self):
        """VERIFY 'Default List' & 'New list' IN SCROLL MENU"""
        info(logger, f"\nStarting Test: {inspect.stack()[0][3]}")
        tasks = TaskListPage(self.driver)
        expect(tasks.verify_list_in_menu(DEFAULT_LIST_NAMES))
        expect('Default List' == tasks.get_active_menu_tab())
        assert_expectations()

    def test_create_new_list(self):
        """VERIFY NEW LIST CAN BE CREATED"""
        info(logger, f"\nStarting Test: {inspect.stack()[0][3]}")
        tasks = TaskListPage(self.driver)
        tasks.click_new_list()
        new_list = NewListPage(self.driver)
        new_list.create_new_list(LIST_NAME_01)
        expect(tasks.empty_list.is_displayed())
        expect('No tasks yet' == tasks.empty_list.get_text())
        assert_expectations()

    def test_delete_existing_list(self):
        """VERIFY EXISTING LIST CAN BE DELETED"""
        info(logger, f"\nStarting Test: {inspect.stack()[0][3]}")
        menu = MenuDrawerPage(self.driver)
        menu.prompt_menu_drawer()
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="Create new list"]').click()
        new_list = NewListPage(self.driver)
        new_list.create_new_list(LIST_NAME_02)
        options = OptionsDrawerPage(self.driver)
        options.prompt_options_drawer()
        self.driver.find_element_by_xpath('//XCUIElementTypeCell[@name="Delete list"]').click()
        tasks = TaskListPage(self.driver)
        expect(LIST_NAME_02 not in tasks.get_all_list_names())
        menu.prompt_menu_drawer()
        expect(LIST_NAME_02 not in menu.get_all_lists_names())
        assert_expectations()

    def test_unable_delete_default_list(self):
        """VERIFY DEFAULT LIST CAN NOT BE DELETED"""
        info(logger, f"\nStarting Test: {inspect.stack()[0][3]}")
        task = TaskListPage(self.driver)
        task.click_default_list()
        options = OptionsDrawerPage(self.driver)
        options.prompt_options_drawer()
        expect(options.delete_list.get_attribute('enabled') == 'false')

    def test_update_list_name(self):
        """"VERIFY EXISTING LIST NAME CAN BE UPDATED"""
        info(logger, f"\nStarting Test: {inspect.stack()[0][3]}")
        menu = MenuDrawerPage(self.driver)
        menu.prompt_menu_drawer()
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="Create new list"]').click()
        new_list = NewListPage(self.driver)
        new_list.create_new_list(LIST_NAME_02)
        options = OptionsDrawerPage(self.driver)
        options.prompt_options_drawer()
        self.driver.find_element_by_xpath('//XCUIElementTypeCell[@name="Rename list"]').click()
        update_list = NewListPage(self.driver)
        update_list.create_new_list(UPDATED_LIST_NAME_02)
        tasks = TaskListPage(self.driver)
        expect(LIST_NAME_02 not in tasks.get_all_list_names())
        expect(UPDATED_LIST_NAME_02 in tasks.get_all_list_names())
        menu.prompt_menu_drawer()
        expect(LIST_NAME_02 not in menu.get_all_lists_names())
        expect(UPDATED_LIST_NAME_02 in menu.get_all_lists_names())

    def test_unable_delete_all_empty_list(self):
        """VERIFY 'Delete All' OPTION DISABLED FOR EMPTY LIST"""
        info(logger, f"\nStarting Test: {inspect.stack()[0][3]}")
        task = TaskListPage(self.driver)
        task.click_default_list()
        options = OptionsDrawerPage(self.driver)
        options.prompt_options_drawer()
        expect(options.delete_all_completed.get_attribute('enabled') == 'false')
