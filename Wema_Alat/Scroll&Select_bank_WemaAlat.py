from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


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


email = "akpanudootobong@gmail.com"
password = "Nsisong03."


loginBtn = driver.find_element(AppiumBy.ID,'com.wemabank.alat.prod:id/loginBtn')
loginBtn.click()

email_Input = wait.until(EC.visibility_of_element_located((By.ID, 'com.wemabank.alat.prod:id/email_input')))
email_Input.send_keys(email)

password_Input = driver.find_element(AppiumBy.ID, 'com.wemabank.alat.prod:id/password_input')
password_Input.send_keys(password)

loginBtn2 = driver.find_element(AppiumBy.ID, 'com.wemabank.alat.prod:id/loginBtn')
loginBtn2.click()

Cancel = wait.until(EC.visibility_of_element_located((By.ID, 'com.wemabank.alat.prod:id/cancelText')))
Cancel.click()

Send_money = wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Send Money']")))
Send_money.click()

To_bank_account = wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='To Bank Account']")))
To_bank_account.click()

Select_Bank_input = wait.until(EC.visibility_of_element_located((By.ID, 'com.wemabank.alat.prod:id/select_bank_text')))
Select_Bank_input.click()

# Single scroll

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(349, 1076)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(351, 740)
actions.w3c_actions.pointer_action.release()
actions.perform()

# Multiple scrolls

for i in range(20):
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(341, 1423)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(389, 762)
    actions.w3c_actions.pointer_action.release()
    actions.perform()

GT_bank = wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='GUARANTY TRUST BANK']")))
confirm_bank_name = GT_bank.get_attribute("text")

assert confirm_bank_name == "GUARANTY TRUST BANK", "Invalid Bank"

GT_bank.click()

