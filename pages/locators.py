from appium.webdriver.common.mobileby import MobileBy
from utils.setup.wrapper import UiWrapper


class TasksScreen:
    LIST_SCROLL_MENU = UiWrapper(MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther'
                                                   '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                                   '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                                   '/XCUIElementTypeOther[1]/XCUIElementTypeOther['
                                                   '2]/XCUIElementTypeScrollView')
    DEFAULT_LIST_TAB = UiWrapper(MobileBy.ACCESSIBILITY_ID, 'Default List')
    NEW_LIST_TAB = UiWrapper(MobileBy.ACCESSIBILITY_ID, 'New list')
    EMPTY_LIST_TEXT = UiWrapper(MobileBy.ACCESSIBILITY_ID, 'No tasks yet')
    ITEM_CONTAINER = UiWrapper(MobileBy.XPATH, '//XCUIElementTypeApplication['
                                              '@name="Tasks"]/XCUIElementTypeWindow/XCUIElementTypeOther'
                                              '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                              '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                              '/XCUIElementTypeOther[1]/XCUIElementTypeOther['
                                              '1]/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther'
                                              '/XCUIElementTypeCollectionView')


class CreateNewList:
    CLOSE_BTN = UiWrapper(MobileBy.ACCESSIBILITY_ID, 'Cancel')
    DONE_BTN = UiWrapper(MobileBy.XPATH, '//XCUIElementTypeButton[@name="Done"]')
    HEADER = UiWrapper(MobileBy.ACCESSIBILITY_ID, 'Create new list')
    TITLE_INPUT = UiWrapper(MobileBy.XPATH, '//XCUIElementTypeApplication[@name="Tasks"]/XCUIElementTypeWindow['
                                           '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                           '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                           '/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTextField')


class BottomNav:
    LIST_MENU = UiWrapper(MobileBy.ACCESSIBILITY_ID, 'Task lists menu')
    ADD_NEW_TASK = UiWrapper(MobileBy.ACCESSIBILITY_ID, 'Add a new task')
    LIST_OPTIONS = UiWrapper(MobileBy.ACCESSIBILITY_ID, 'List options')
    BACK_NAV_CHEVRON = UiWrapper(MobileBy.ACCESSIBILITY_ID, 'back_bar_button')


class OptionsDrawer:
    MY_SORT = UiWrapper(MobileBy.ACCESSIBILITY_ID, 'Sort by my order')
    DATE_SORT = UiWrapper(MobileBy.ACCESSIBILITY_ID, 'Sort by date')
    RENAME_LIST = UiWrapper(MobileBy.XPATH, '//XCUIElementTypeCell[@name="Rename list"]')
    DELETE_LIST = UiWrapper(MobileBy.XPATH, '//XCUIElementTypeCell[@name="Delete list"]')
    DELETE_ALL_TASKS = UiWrapper(MobileBy.XPATH, '//XCUIElementTypeCell[@name="Delete all completed tasks"]')


class MenuDrawer:
    LIST_CONTAINER = UiWrapper(MobileBy.XPATH, '//XCUIElementTypeScrollView['
                                              '@name="kMDCBottomDrawerScrollViewAccessibilityIdentifier'
                                              '"]/XCUIElementTypeCollectionView')
    DEFAULT_LIST = UiWrapper(MobileBy.XPATH, '//XCUIElementTypeScrollView['
                                            '@name="kMDCBottomDrawerScrollViewAccessibilityIdentifier'
                                            '"]/XCUIElementTypeCollectionView/XCUIElementTypeCell[1]')
    CREATE_NEW_LIST = UiWrapper(MobileBy.ACCESSIBILITY_ID, 'Create new list')


class NewTaskDrawer:
    NEW_TASK_INPUT = UiWrapper(MobileBy.ACCESSIBILITY_ID, 'New task title')
    TASK_DETAILS_INPUT = UiWrapper(MobileBy.ACCESSIBILITY_ID, 'Task details')
    REPEAT_TAG = UiWrapper(MobileBy.XPATH, '//XCUIElementTypeButton[@name="Repeating"][2]')
    REMOVE_REPEAT = UiWrapper(MobileBy.ACCESSIBILITY_ID, 'Remove repeating')
    DETAILS_ICON = UiWrapper(MobileBy.ACCESSIBILITY_ID, 'Add details')
    CALENDAR_ICON = UiWrapper(MobileBy.ACCESSIBILITY_ID, 'Add date/time')
    SAVE_BTN = UiWrapper(MobileBy.XPATH, '//XCUIElementTypeButton[@name="Save"]')


class CalendarDrawer:
    HEADER = UiWrapper(MobileBy.ACCESSIBILITY_ID, 'Date & Time')
    DONE_BTN = UiWrapper(MobileBy.XPATH, '//XCUIElementTypeButton[@name="Done"]')
    PREV_MONTH = UiWrapper(MobileBy.ACCESSIBILITY_ID, 'Previous month')
    NEXT_MONTH = UiWrapper(MobileBy.ACCESSIBILITY_ID, 'Next month')
    DEFAULT_SET_TIME = UiWrapper(MobileBy.ACCESSIBILITY_ID, 'Set time')
    DEFAULT_SET_REPEAT = UiWrapper(MobileBy.ACCESSIBILITY_ID, 'Does not repeat')
    REMOVE_TIME = UiWrapper(MobileBy.ACCESSIBILITY_ID, 'Remove time')
    REPEAT_CHEVRON = UiWrapper(MobileBy.XPATH, '//XCUIElementTypeCell['
                                              '@name="GTEDateTimeRecurrencePickerRecurrenceCellA11yID'
                                              '"]/XCUIElementTypeImage[2]')


class RepeatSelection:
    CLOSE_BTN = UiWrapper(MobileBy.ACCESSIBILITY_ID, 'Cancel')
    HEADER = UiWrapper(MobileBy.ACCESSIBILITY_ID, 'Repeat')
    CHECK_ICON = UiWrapper(MobileBy.ACCESSIBILITY_ID, 'ic_check')
    NO_REPEAT_OPTION = UiWrapper(MobileBy.XPATH, '//XCUIElementTypeCell[@name="Does not repeat"]')
    DAILY_REPEAT_OPTION = UiWrapper(MobileBy.XPATH, '//XCUIElementTypeCell[@name="Every day"]')
    YEARLY_REPEAT_OPTION = UiWrapper(MobileBy.XPATH, '//XCUIElementTypeCell[@name="Every year"]')


class ConfirmDeleteDialog:
    WRAPPER = UiWrapper(MobileBy.XPATH, '//XCUIElementTypeApplication[@name="Tasks"]/XCUIElementTypeWindow['
                                        '1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]')


class ConfirmTaskDiscardDialog:
    WRAPPER = UiWrapper(MobileBy.XPATH, '//XCUIElementTypeApplication[@name="Tasks"]/XCUIElementTypeWindow['
                                        '1]/XCUIElementTypeOther[3]/XCUIElementTypeOther[3]')


class TaskDetails:
    TASK_TITLE = UiWrapper(MobileBy.ACCESSIBILITY_ID, 'Task title')
    TASK_DESCRIPTION = UiWrapper(MobileBy.ACCESSIBILITY_ID, 'Task details')
    DELETE_ICON = UiWrapper(MobileBy.ACCESSIBILITY_ID, 'Delete')
    MARK_COMPLETE = UiWrapper(MobileBy.ACCESSIBILITY_ID, 'Mark completed')
    MARK_UNCOMPLETE = UiWrapper(MobileBy.ACCESSIBILITY_ID, 'Mark uncompleted')
