import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

desired_cap = {
    "platformName": "Android",
    "appium:platformVersion": "11.0",
    "appium:deviceName": "R58M750MQ9R",
    "appium:appPackage": "com.tinder",
    "appium:appActivity": "com.tinder.activities.LoginActivity",
    "automationName": "UiAutomator2",
    "newCommandTimeout": "120"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
wait = WebDriverWait(driver, 20)

"""login_btn = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.Button[@text='LOG IN WITH GOOGLE']")))
login_btn.click()

email = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='otakpanudo@gmail.com']")))
email.click()

cancel = wait.until(EC.visibility_of_element_located((By.ID, 'com.google.android.gms:id/cancel')))
cancel.click()

Input_phone_num = wait.until(EC.visibility_of_element_located((By.ID, 'com.tinder:id/phoneNumberInputView')))
Input_phone_num.send_keys("07038799273")


Continue_btn = wait.until(EC.element_to_be_clickable((By.ID, 'com.tinder:id/continueButton')))
Continue_btn.click()

wait.until(EC.element_attribute_to_include((By.XPATH, "//android.widget.EditText[@bounds='[558,318][657,420]'", 'text')))

Continue_btn2 = wait.until(EC.element_to_be_clickable((By.ID, 'com.tinder:id/continueButton')))
Continue_btn2.click()"""

Permission_btn = wait.until(EC.visibility_of_element_located((By.ID, 'com.tinder:id/requestPermissionButton')))
Permission_btn.click()

Allow_btn = wait.until(EC.visibility_of_element_located((By.ID, 'com.android.permissioncontroller:id/permission_allow_foreground_only_button')))
Allow_btn.click()

wait.until(EC.visibility_of_element_located((By.ID, 'com.tinder:id/video_preview_view')))

# swipe left

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(483, 735)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(169, 732)
actions.w3c_actions.pointer_action.release()
actions.perform()

# swipe right 3 times

for i in range(3):
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(169, 732)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(483, 735)
    actions.w3c_actions.pointer_action.release()
    actions.perform()

# tap unlike button

unlike_btn = driver.find_element(By.XPATH, '//android.widget.FrameLayout[@content-desc="Pass"]/android.widget.ImageView')
unlike_btn.click()

# tap like button

like_btn = driver.find_element(By.XPATH, '//android.widget.FrameLayout[@content-desc="Like"]/android.widget.ImageView')
like_btn.click()

# tap message icon

message_btn = driver.find_element(By.XPATH, '//android.widget.FrameLayout[@content-desc="Matches"]/android.widget.ImageView')
message_btn.click()

time.sleep(5)

driver.quit()



