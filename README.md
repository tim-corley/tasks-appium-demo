# Appium Demo

## End-to-End Testing Against the Google Task Native iOS Application

---

## PREREQUISITES

- MacOS
- iPhone
- Python3.7
- pipenv  
- NodeJS / NPM  
- Xcode
- USB-C/Lightning Cable
- Google Account
- Apple Developer Account  
- Git

## Tested with Following Configuration:
| Application      | Version      |
| -----------      | -----------  |
| iPhone           | 11           |
| iOS              | 14.8         |
| MacOS            | Big Sur 11.6 |
| Xcode            | 13.0         |
| Appium           | 1.21         |
| Google Tasks     | 1.38         |

---

## Running Tests

### 1) Collect Desired Capabilities
You will need some specific info regarding the application you are testing as well as the device being used.

#### DEVICE

A) Connect the test device (iPhone) to a MacOS computer

B) Open the Finder app & select the device from the list on the left

C) Note the device name

D) Click on device name / header menu to cycle through some sets of data

   - second set should contain the device's UDID

Alternatively, to get device name and udid via the terminal, use:
```shell
instruments -s devices
```

#### APPLICATION

A) Install Application via [App Store](https://apps.apple.com/us/app/google-tasks-get-things-done/id1353634006) to device

B) Connect Phone to Computer

C) Launch "Console" App from MacOS

D) Launch the Application on the phone

E) Use Search within Console App (search term - application name) to find the bundleId
  - look for "SpringBoard" in the Process column
  - look for Message such as: "Creating process for executionContext with identity: application<com.google.tasks>"
  - "com.google.tasks" is the bundleId

**Add this data to the `utils/setup/capabilities` module**

### 2) Install WebDriverAgent Application to the test device

A) Clone the [WDA Repo](https://github.com/appium/WebDriverAgent) (Appium Fork)

B) Open WebDriverAgent project in Xcode

C) Select WebDriverAgentRunner target

D) Update Signing > Team to your personal developer account

E) Update Build Settings > Packaging > Product Bundle Identifier

F) Build the app (Product > Build)

G) Connect iPhone to Mac Computer

H) Select Device from WebDriverAgentRunner Schema Dropdown

I) Install WebDriverAgentRunner to Device (Product > Test)
 - If error shown in Xcode, on the iPhone, navigate to: Settings > General > Device Management > Developer > Trust the App
 - Once WebDriverAgentRunner is trusted / verified on deivce try Product > Test again

### 3) Install and Run Appium Server

A) Install [Appium with NPM](https://www.npmjs.com/package/appium)
```shell
npm -g appium
```

B) Run Appium
```shell
appium
```

### 4) Install Dependencies & Activate Virtual Environment (w/ pipenv)
 - Navigate to root directory and run:
```shell
pipenv install
```

```shell
pipenv shell
```

### 5) Trigger Test Run
 - Using the pytest syntax / conventions, trigger the tests you'd like to run (be sure you have the virtualenv activated)

A) Run all tests (with print statements enabled):
```shell
python -m pytest -s 
```

B) Run all tests from a specified module:
```shell
python -m pytest test_list_actions.py
```

C) Run all tests from a specified class:
```shell
python -m pytest test_task_actions::TestTaskDetailsSuite
```

D) Run a single test method:
```shell
python -m pytest test_task_actions::TestTaskDetailsSuite:: test_task_marked_complete
```
