from appium.webdriver.common.mobileby import MobileBy
from pages.locators import ConfirmDeleteDialog, ConfirmTaskDiscardDialog
from utils.logs.testlogger import Logger, info, error
from pages.base_page import BasePage


logger = Logger().get_logger()


class ConfirmActionDialogPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.delete_wrapper = ConfirmDeleteDialog.WRAPPER
        self.discard_wrapper = ConfirmTaskDiscardDialog.WRAPPER

    def select_delete(self):
        try:
            options = self.delete_wrapper.get_all_child_elements(MobileBy.CLASS_NAME, 'XCUIElementTypeScrollView')
            delete_btn = options[2].find_element_by_xpath('//XCUIElementTypeButton[@name="Delete"]')
            delete_btn.click()
        except AssertionError:
            error(logger, 'unable to select "Delete" from confirmation dialog')
            pass

    def select_discard(self):
        try:
            options = self.discard_wrapper.get_all_child_elements(MobileBy.CLASS_NAME, 'XCUIElementTypeScrollView')
            discard_btn = options[2].find_element_by_xpath('//XCUIElementTypeButton[@name="Discard"]')
            discard_btn.click()
        except AssertionError:
            error(logger, 'unable to select "Discard" from confirmation dialog')
            pass

    def select_cancel(self):
        try:
            options = self.delete_wrapper.get_all_child_elements(MobileBy.CLASS_NAME, 'XCUIElementTypeScrollView')
            cancel_btn = options[2].find_element_by_xpath('//XCUIElementTypeButton[@name="Cancel"]')
            cancel_btn.click()
        except AssertionError:
            error(logger, 'unable to select "Cancel" from confirmation dialog')
            pass
