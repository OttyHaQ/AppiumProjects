import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

desired_cap = {
    "platformName": "Android",
    "appium:platformVersion": "11.0",
    "appium:deviceName": "R58M750MQ9R",
    "appium:appPackage": "com.bumble.app",
    "appium:appActivity": "com.bumble.app.ui.launcher.BumbleLauncherActivity",
    "automationName": "UiAutomator2",
    "newCommandTimeout": "120",
    "autoGrantPermissions": ""
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
wait = WebDriverWait(driver, 20)

Mobile_num_signIn = wait.until(EC.visibility_of_element_located((By.ID, 'com.bumble.app:id/landing_manualLoginButton')))
Mobile_num_signIn.click()

time.sleep(3)

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(339, 962)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

# searching
#search_element = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'SomeAccessibilityID').send_keys("iphone")
# Or
# driver.set_value(search_element, 'iphone')
# or
# driver.press_keycode(84)
# or
# driver.execute_script('mobile: performEditorAction', ('action': 'search'))

# common actions include go, send, next, done, previous


