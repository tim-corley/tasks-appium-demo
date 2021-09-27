from pages.base_page import BasePage
from pages.locators import NewTaskDrawer
from utils.logs.testlogger import Logger, info, error

logger = Logger().get_logger()


class NewTaskDrawerPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.new_task_input = NewTaskDrawer.NEW_TASK_INPUT
        self.task_details_input = NewTaskDrawer.TASK_DETAILS_INPUT
        self.details_icon = NewTaskDrawer.DETAILS_ICON
        self.save_btn = NewTaskDrawer.SAVE_BTN

    def input_task_title(self, task_title):
        try:
            self.new_task_input.set_text(str(task_title))
        except AssertionError:
            error(logger, 'unable to input title for new task')

    def create_new_task(self, task_title, description=None):
        try:
            if description:
                self.new_task_input.set_text(str(task_title))
                self.details_icon.click()
                self.task_details_input.set_text(str(description))
                self.save_btn.click()
                info(logger, 'successfully input new task title, task description, & clicked save')
            else:
                self.new_task_input.set_text(str(task_title))
                self.save_btn.click()
                info(logger, 'successfully input new task title & clicked save')
        except AssertionError:
            error(logger, 'unable to create new task')
