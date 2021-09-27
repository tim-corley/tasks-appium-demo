from pages.locators import CreateNewList
from utils.logs.testlogger import Logger, info, error

logger = Logger().get_logger()


class NewListPage:

    def __init__(self, driver):
        self.driver = driver
        self.header = CreateNewList.HEADER
        self.close_btn = CreateNewList.CLOSE_BTN
        self.done_btn = CreateNewList.DONE_BTN
        self.title_input = CreateNewList.TITLE_INPUT

    def get_header_text(self):
        try:
            return str(self.header.get_text())
        except AssertionError:
            error(logger, 'unable to get text for new list page header')

    def click_close(self):
        try:
            self.close_btn.click()
            info(logger, 'clicked close button')
        except AssertionError:
            error(logger, 'unable to click close button')
            pass

    def create_new_list(self, list_title):
        try:
            self.title_input.set_text(str(list_title))
            self.done_btn.click()
            info(logger, 'successfully input new list title & clicked done')
        except AssertionError:
            error(logger, 'unable to create new list')
