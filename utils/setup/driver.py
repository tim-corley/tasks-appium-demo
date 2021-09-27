import logging
import threading
from appium import webdriver
from utils.logs.testlogger import info, error
from utils.setup.capabilities import DesiredCapabilities

logger = logging.getLogger('utils/logs/testlogs.log')


class Driver:
    __DRIVER_MAP = {}

    @staticmethod
    def initialize_driver():
        thread_object = threading.currentThread()

        def driver_config(driver=None):
            try:
                driver = webdriver.Remote(
                    command_executor='http://127.0.0.1:4723/wd/hub',
                    desired_capabilities=DesiredCapabilities().get_device_capabilities())
                # driver.implicitly_wait(5)
            except (ValueError, Exception):
                error(logger, "unable to initialize driver.")
            return driver

        Driver.__map(thread_object, driver_config())
        return Driver.get_driver()

    @staticmethod
    def get_driver():
        return Driver.__DRIVER_MAP[threading.current_thread()]["driver"]

    @staticmethod
    def __map(thread, driver):
        Driver.__DRIVER_MAP[thread] = {"driver": driver}

    @staticmethod
    def start(target):
        Driver.get_driver().get(target)

    @staticmethod
    def shutdown():
        Driver.get_driver().close_app()
        Driver.get_driver().quit()
        info(logger, 'Successfully Closed App & Ended the Session.')
