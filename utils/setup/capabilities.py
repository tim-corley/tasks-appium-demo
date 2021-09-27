class DesiredCapabilities:
    ios_phone = {
        'platformName': 'iOS',
        'deviceName': "Tim’s iPhone",
        'udid': "00008030-001C21D00CC3402E",
        'bundleId': 'com.google.tasks',
        'automationName': 'XCUITest',
        'platformVersion': '14.8'
    }

    def get_device_capabilities(self):
        return self.ios_phone
