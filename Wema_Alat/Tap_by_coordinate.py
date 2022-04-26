
from appium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.ui import WebDriverWait


desired_cap = {
    "platformName": "Android",
    "appium:platformVersion": "11.0",
    "appium:deviceName": "R58M750MQ9R",
    "appium:appPackage": "com.wemabank.alat.prod",
    "appium:appActivity": "crc64944946ad7d7f913c.LandingPageActivity",
    "automationName": "UiAutomator2",
    "newCommandTimeout": "120",
    "autoGrantPermissions": "true"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
wait = WebDriverWait(driver, 20)

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(523, 1201)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

