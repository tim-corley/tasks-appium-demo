import inspect
from GLOBALS import *
from tests.base_test import BlankListStartTest, SampleListStartTest
from pages.page_tasks import TaskListPage
from pages.drawer_new_task import NewTaskDrawerPage
from pages.page_task_details import TaskDetailsPage
from pages.dialog_confirm import ConfirmActionDialogPage
from delayed_assert import expect, assert_expectations
from utils.logs.testlogger import Logger, info

logger = Logger().get_logger()


class TestTaskCreateSuite(BlankListStartTest):

    def test_create_new_task(self):
        """VERIFY NEW TASK ADDED TO LIST W/ TITLE"""
        info(logger, f"\nStarting Test: {inspect.stack()[0][3]}")
        new_task = NewTaskDrawerPage(self.driver)
        new_task.prompt_add_new_task_drawer()
        new_task.create_new_task(TASK_NAME_01)
        task_list = TaskListPage(self.driver)
        expect(TASK_NAME_01 in task_list.get_all_incomplete_item_titles())

    def test_create_task_details(self):
        """VERIFY NEW TASK ADDED TO LIST W/ TITLE & DESCRIPTION"""
        info(logger, f"\nStarting Test: {inspect.stack()[0][3]}")
        new_task = NewTaskDrawerPage(self.driver)
        new_task.prompt_add_new_task_drawer()
        new_task.create_new_task(TASK_NAME_01, TASK_DETAIL_01)
        task_list = TaskListPage(self.driver)
        task_list.select_task(TASK_NAME_01)
        task_detail = TaskDetailsPage(self.driver)
        expect(TASK_NAME_01 in task_detail.get_task_title())
        expect(TASK_DETAIL_01 in task_detail.get_task_description())
        task_detail.select_back_nav_chevron()

    def test_handle_junk_inputs(self):
        """VERIFY ADDING TASK WORKS WITH UNUSUAL DATA"""
        info(logger, f"\nStarting Test: {inspect.stack()[0][3]}")
        new_task = NewTaskDrawerPage(self.driver)
        new_task.prompt_add_new_task_drawer()
        new_task.create_new_task(JUNK_01, JUNK_02*3)
        task_list = TaskListPage(self.driver)
        task_list.select_task(JUNK_01)
        task_detail = TaskDetailsPage(self.driver)
        expect(JUNK_01 in task_detail.get_task_title())
        expect(JUNK_02 in task_detail.get_task_description())
        task_detail.select_back_nav_chevron()

    def test_task_discard(self):
        """VERIFY ADD TASK DRAWER DISMISSED WHEN TAPPING ABOVE IT"""
        info(logger, f"\nStarting Test: {inspect.stack()[0][3]}")
        new_task = NewTaskDrawerPage(self.driver)
        new_task.prompt_add_new_task_drawer()
        new_task.input_task_title(TASK_NAME_01)
        new_task.tap_screen(207, 300)
        dialog = ConfirmActionDialogPage(self.driver)
        info(logger, 'confirming task discard via dialog')
        dialog.select_discard()
        tasks = TaskListPage(self.driver)
        expect(tasks.empty_list.is_displayed())


class TestTaskDetailsSuite(SampleListStartTest):

    def test_task_marked_complete(self):
        """VERIFY MARKING TASK AS COMPLETE MOVES IT TO 'COMPLETED' SECTION"""
        info(logger, f"\nStarting Test: {inspect.stack()[0][3]}")
        tasks = TaskListPage(self.driver)
        tasks.click_custom_list(LIST_NAME_03)
        tasks.select_item_status_radio_btn()
        tasks = TaskListPage(self.driver)
        all_tasks = tasks.get_all_list_items()
        expect(SAMPLE_TASKS[-1] in all_tasks["complete_items"])
        expect(all_tasks["complete_count"] == 1)
        expect(SAMPLE_TASKS[-1] not in all_tasks["incomplete_items"])
        assert_expectations()

    def test_task_marked_uncompleted(self):
        """VERIFY MARKING TASK AS UNCOMPLETED MOVES IT OUT OF 'COMPLETED' SECTION"""
        info(logger, f"\nStarting Test: {inspect.stack()[0][3]}")
        tasks = TaskListPage(self.driver)
        tasks.click_custom_list(LIST_NAME_03)
        tasks.select_item_status_radio_btn()
        # VERIFY TASK MOVED TO COMPLETED SECTION
        all_tasks = tasks.get_all_list_items()
        expect(SAMPLE_TASKS[-1] in all_tasks["complete_items"])
        expect(all_tasks["complete_count"] == 1)
        # MARK AS UNCOMPLETED
        tasks.select_task(SAMPLE_TASKS[-1])
        task_details = TaskDetailsPage(self.driver)
        task_details.click_mark_uncomplete()
        task_details.select_back_nav_chevron()
        all_tasks = tasks.get_all_list_items()
        expect(all_tasks["incomplete_count"] == 3)
        expect(all_tasks["complete_count"] == 0)
        assert_expectations()

    def test_tasks_deleted(self):
        """VERIFY USERS CAN DELETE A TASK"""
        info(logger, f"\nStarting Test: {inspect.stack()[0][3]}")
        tasks = TaskListPage(self.driver)
        all_tasks = tasks.get_all_list_items()
        expect(all_tasks["incomplete_count"] == 3)
        for task in SAMPLE_TASKS:
            tasks.select_task(task)
            task_details = TaskDetailsPage(self.driver)
            task_details.click_delete_icon()
        expect(tasks.empty_list.is_displayed())
        assert_expectations()