from appium.webdriver.common.touch_action import TouchAction
from utils.logs.testlogger import Logger, info, error
from pages.locators import BottomNav

logger = Logger().get_logger()


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.nav_menu = BottomNav.LIST_MENU
        self.nav_add = BottomNav.ADD_NEW_TASK
        self.nav_options = BottomNav.LIST_OPTIONS
        self.back_nav = BottomNav.BACK_NAV_CHEVRON

    def prompt_menu_drawer(self):
        try:
            self.nav_menu.click()
            info(logger, 'clicked menu icon from bottom nav')
        except AssertionError:
            error(logger, 'unable to click menu from bottom nav')
            pass

    def prompt_add_new_task_drawer(self):
        try:
            self.nav_add.click()
            info(logger, 'clicked add icon from bottom nav')
        except AssertionError:
            error(logger, 'unable to click add from bottom nav')
            pass

    def prompt_options_drawer(self):
        try:
            self.nav_options.click()
            info(logger, 'clicked options icon from bottom nav')
        except AssertionError:
            error(logger, 'unable to click options from bottom nav')
            pass

    def select_back_nav_chevron(self):
        try:
            self.back_nav.click()
            info(logger, 'clicked back navigation chevron')
        except AssertionError:
            error(logger, 'unable to click back nav chevron')
            pass

    def tap_screen(self, x, y):
        """use tap away from a drawer to close it"""
        actions = TouchAction(self.driver)
        actions.tap(None, x, y).perform()
