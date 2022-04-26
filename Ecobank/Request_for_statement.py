from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

desired_cap = {
    "platformName": "Android",
    "appium:platformVersion": "11.0",
    "appium:deviceName": "R58M750MQ9R",
    "appium:appPackage": "com.app.ecobank",
    "appium:appActivity": "com.app.ecobank.ui.splash.SplashActivity",
    "automationName": "UiAutomator2"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
wait = WebDriverWait(driver, 20)

Get_Started_Btn = wait.until(EC.visibility_of_element_located((By.ID, 'com.app.ecobank:id/appcpbtn_getstart')))
Get_Started_Btn.click()

Yes_btn = wait.until(EC.visibility_of_element_located((By.ID, 'com.app.ecobank:id/appcpbtn_yes')))
Yes_btn.click()

wait.until(EC.visibility_of_element_located((By.ID, 'com.app.ecobank:id/txt_label_select_country_button')))


actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(207, 334)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()


Benin = wait.until(EC.visibility_of_element_located((By.XPATH, '//android.widget.TextView[@text="Benin"]')))

for i in range(5):
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(341, 1213)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(339, 902)
    actions.w3c_actions.pointer_action.release()
    actions.perform()

Nigeria = wait.until(EC.visibility_of_element_located((By.XPATH, '//android.widget.TextView[@text="Nigeria"]')))
Nigeria.click()

input_phone_num = wait.until(EC.visibility_of_element_located((By.ID, 'com.app.ecobank:id/edt_mobile_number_verify')))
input_phone_num.send_keys("07038799273")

continue_btn = wait.until(EC.visibility_of_element_located((By.ID, 'com.app.ecobank:id/btn_continue')))
continue_btn.click()

wait.until(EC.visibility_of_element_located((By.ID, 'com.app.ecobank:id/text_message')))

driver.find_element(by=AppiumBy.ID, value="com.app.ecobank:id/t9_key_3").click()
driver.find_element(by=AppiumBy.ID, value="com.app.ecobank:id/t9_key_9").click()
driver.find_element(by=AppiumBy.ID, value="com.app.ecobank:id/t9_key_6").click()
driver.find_element(by=AppiumBy.ID, value="com.app.ecobank:id/t9_key_1").click()
driver.find_element(by=AppiumBy.ID, value="com.app.ecobank:id/t9_key_0").click()
driver.find_element(by=AppiumBy.ID, value="com.app.ecobank:id/t9_key_7").click()

Use_debit_card = wait.until(EC.visibility_of_element_located((By.ID, 'com.app.ecobank:id/txt_sub_title')))
Use_debit_card.click()




