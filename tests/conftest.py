import pytest
from appium.webdriver.common.touch_action import TouchAction
from GLOBALS import *
from pages.drawer_menu import MenuDrawerPage
from pages.page_tasks import TaskListPage
from pages.drawer_new_task import NewTaskDrawerPage
from pages.page_new_list import NewListPage
from pages.dialog_confirm import ConfirmActionDialogPage
from utils.logs.testlogger import Logger, info, error
from utils.setup.driver import Driver

logger = Logger().get_logger()


@pytest.fixture(scope="function")
def setup(request):
    try:
        driver = Driver.initialize_driver()
        info(logger, 'Driver Session Successfully Initialized.')
        request.cls.driver = driver
        yield
        # TAP @ TOP/MID SCREEN TO CLOSE ANY DRAWERS
        actions = TouchAction(driver)
        # actions.tap(None, 207, 300).perform()
        actions.tap(None, 60, 120).perform()
        tasks = TaskListPage(driver)
        # tasks.click_default_list()
        menu = MenuDrawerPage(driver)
        menu.prompt_menu_drawer()
        to_delete = list(filter(lambda lst: lst not in PERM_MENU_ITEMS, menu.get_all_lists_names()))
        if to_delete:
            info(logger, 'Deleting All Lists Created Via Test Suite...')
            for d in to_delete:
                menu.select_item(d)
                list_items = tasks.get_all_incomplete_item_titles()
                menu.prompt_options_drawer()
                delete_btn = driver.find_element_by_xpath('//XCUIElementTypeCell[@name="Delete list"]')
                info(logger, 'Clicking Delete Via Option Drawer')
                delete_btn.click()
                if list_items:
                    dialog = ConfirmActionDialogPage(driver)
                    info(logger, 'Confirming Delete Via Dialog')
                    dialog.select_delete()
                menu.prompt_menu_drawer()
        Driver.shutdown()
        info(logger, 'Driver Session Successfully Terminated.')
    except AssertionError:
        error(logger, 'Unable to Initialize Driver Session')


@pytest.fixture(scope="function")
def blank_list(request):
    tasks = TaskListPage(request.cls.driver)
    tasks.click_new_list()
    new_list = NewListPage(request.cls.driver)
    new_list.create_new_list(LIST_NAME_03)


@pytest.fixture(scope="function")
def sample_list(request):
    new_task = NewTaskDrawerPage(request.cls.driver)
    for task in SAMPLE_TASKS:
        new_task.prompt_add_new_task_drawer()
        new_task.create_new_task(task)
