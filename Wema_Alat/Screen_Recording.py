import base64
import time
import os.path
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
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

# start recording here

driver.start_recording_screen()

loginBtn = driver.find_element(AppiumBy.ID,'com.wemabank.alat.prod:id/loginBtn')
loginBtn.click()

email_Input = wait.until(EC.visibility_of_element_located((By.ID, 'com.wemabank.alat.prod:id/email_input')))
email_Input.send_keys(email)

password_Input = driver.find_element(AppiumBy.ID, 'com.wemabank.alat.prod:id/password_input')
password_Input.send_keys(password)

loginBtn2 = driver.find_element(AppiumBy.ID,'com.wemabank.alat.prod:id/loginBtn')
loginBtn2.click()

Cancel = wait.until(EC.visibility_of_element_located((By.ID, 'com.wemabank.alat.prod:id/cancelText')))
Cancel.click()

# stop recording here

video_raw_data = driver.stop_recording_screen()
timeStamp = time.strftime("%Y_%m_%d_%H%M%S")
file_name = driver.current_activity + timeStamp

# create filepath to save video

filepath = os.path.join("C:/Users/INY/AppiumProjects/ScreenShots/", file_name+".mp4")

with open(filepath, "wb") as vd:
    vd.write(base64.b64decode(video_raw_data))