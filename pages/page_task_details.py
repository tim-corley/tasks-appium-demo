from pages.base_page import BasePage
from pages.locators import TaskDetails
from utils.logs.testlogger import Logger, info, error

logger = Logger().get_logger()


class TaskDetailsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.task_title = TaskDetails.TASK_TITLE
        self.task_description = TaskDetails.TASK_DESCRIPTION
        self.task_delete_icon = TaskDetails.DELETE_ICON
        self.mark_complete = TaskDetails.MARK_COMPLETE
        self.mark_uncomplete = TaskDetails.MARK_UNCOMPLETE

    def get_task_title(self):
        try:
            return self.task_title.get_text()
        except AssertionError:
            error(logger, 'unable to locate task description text')
            pass

    def get_task_description(self):
        try:
            return self.task_description.get_text()
        except AssertionError:
            error(logger, 'unable to locate task description text')
            pass

    def click_mark_uncomplete(self):
        try:
            self.mark_uncomplete.click()
        except AssertionError:
            error(logger, 'unable to select "Mark uncompleted" from task details screen')
            pass

    def click_delete_icon(self):
        try:
            self.task_delete_icon.click()
        except AssertionError:
            error(logger, 'unable to select delete/trash icon from task details screen')
            pass
