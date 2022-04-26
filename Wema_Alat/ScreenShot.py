
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
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


loginBtn = driver.find_element(AppiumBy.ID,'com.wemabank.alat.prod:id/loginBtn')
loginBtn.click()

timeStamp = time.strftime("%Y_%m_%d_%H%M%S")
file_name = driver.current_activity + timeStamp
time.sleep(3)
driver.save_screenshot("C:/Users/INY/AppiumProjects/ScreenShots/"+file_name+".png")