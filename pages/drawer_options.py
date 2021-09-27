from pages.base_page import BasePage
from pages.locators import OptionsDrawer
from utils.logs.testlogger import Logger, info, error

logger = Logger().get_logger()


class OptionsDrawerPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.rename_list = OptionsDrawer.RENAME_LIST
        self.delete_list = OptionsDrawer.DELETE_LIST
        self.delete_all_completed = OptionsDrawer.DELETE_ALL_TASKS

    def click_rename_list(self):
        try:
            self.rename_list.click()
            info(logger, 'clicked rename list from options menu')
        except AssertionError:
            error(logger, 'unable to click rename list from options menu')
            pass

    def click_delete_list(self):
        try:
            if self.delete_list.is_clickable():
                print('delete list btn can be clicked....')
                self.delete_list.click()
                info(logger, 'deleted list')
            else:
                return "list cannot be deleted"
        except AssertionError:
            error(logger, 'unable to delete list')
            pass

    def delete_all_completed_tasks_from_list(self):
        try:
            if self.delete_all_completed.is_clickable():
                self.delete_all_completed.click()
                info(logger, 'clicked new list tab')
            else:
                return "list does not contain any completed tasks"
        except AssertionError:
            error(logger, 'unable to delete all completed tasks')
            pass
