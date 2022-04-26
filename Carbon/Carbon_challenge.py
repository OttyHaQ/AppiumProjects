
from appium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

desired_cap = {
    "platformName": "Android",
    "appium:platformVersion": "11.0",
    "appium:deviceName": "R58M750MQ9R",
    "app": "C:/Users/INY/Downloads/carbon_ng-v6.7.1_signed.apk",
    "appium:appPackage": "",
    "appium:appActivity": "",
    "automationName": "UiAutomator2",
    "newCommandTimeout": "120",
    "autoGrantPermissions": "true"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
wait = WebDriverWait(driver, 20)
phone_num ="08990001100"
pin = "1234"

Tutorial_msg = wait.until(EC.visibility_of_element_located((By.ID, 'com.lenddo.mobile.paylater.staging:id/tutorial_message')))

for i in range(5):
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(551, 1380)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.w3c_actions.pointer_action.release()
    actions.perform()

Sign_In = wait.until(EC.visibility_of_element_located((By.ID, 'com.lenddo.mobile.paylater.staging:id/user_type_existing')))
Sign_In.click()

Input_Phone_num = wait.until(EC.visibility_of_element_located((By.ID, 'com.lenddo.mobile.paylater.staging:id/sign_in_phone')))
Input_Phone_num.send_keys(phone_num)

Input_pin = wait.until(EC.visibility_of_element_located((By.ID, 'com.lenddo.mobile.paylater.staging:id/sign_in_pin')))
Input_pin.send_keys(pin)

Sign_In_btn = wait.until(EC.visibility_of_element_located((By.ID, 'com.lenddo.mobile.paylater.staging:id/sign_in_next')))
Sign_In_btn.click()





