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
phone_num = "07038799273"
Recharge_Amt = "100"
pin = "3961"

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

airtime_and_data = wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.ScrollView/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.LinearLayout')))
airtime_and_data.click()

buy_Airtime = wait.until(EC.visibility_of_element_located((AppiumBy.ID, 'com.wemabank.alat.prod:id/buy_airtime_btn')))
buy_Airtime.click()

mtn_logo = wait.until(EC.visibility_of_element_located((AppiumBy.ID, 'com.wemabank.alat.prod:id/network_img')))
mtn_logo.click()

phone_num_input = driver.find_element(AppiumBy.ID, 'com.wemabank.alat.prod:id/phone_number')
phone_num_input.send_keys(phone_num)

Amount = driver.find_element(AppiumBy.ID, 'com.wemabank.alat.prod:id/amount')
Amount.send_keys(Recharge_Amt)

Next_Btn = driver.find_element(AppiumBy.ID, 'com.wemabank.alat.prod:id/next_btn')
Next_Btn.click()

Input_pin = wait.until(EC.visibility_of_element_located((AppiumBy.ID, 'com.wemabank.alat.prod:id/pin')))
Input_pin.send_keys(pin)

Confirm_Btn = driver.find_element(AppiumBy.ID, 'com.wemabank.alat.prod:id/confirm_btn')
Confirm_Btn.click()

print("Account Recharged successfully!!!")
