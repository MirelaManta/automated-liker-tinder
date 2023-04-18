from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from dotenv.main import load_dotenv
from time import sleep
import os

chrome_driver_path = r"C:\Development\chromedriver.exe"
service = Service(chrome_driver_path)
chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=chr_options)
load_dotenv()
URL = "https://tinder.com/"
phone_num = os.environ["FB_PHONE"]
fb_password = os.environ["FB_PASS"]

driver.get(URL)
sleep(2)

# Click on Login button
login_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login_button.click()
sleep(2)
# Click on Login with Facebook button
login_fb = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]/div/div')
login_fb.click()
sleep(2)
# Switch to Facebook login window. In order to make selenium work with it, we need to switch to the window in front.
# driver.window_handles   --- This line of code returns a list of all the window handles
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)
sleep(2)
# Allow cookies and login with Facebook credentials
allow_cookies = driver.find_element(By.CSS_SELECTOR, "button[data-cookiebanner='accept_button']")
allow_cookies.click()
sleep(2)
email_input = driver.find_element(By.CSS_SELECTOR, "input[name='email']")
email_input.send_keys(phone_num)
pass_input = driver.find_element(By.CSS_SELECTOR, "input[name='pass']")
pass_input.send_keys(fb_password)
pass_input.send_keys(Keys.ENTER)
sleep(2)
# Switch back to main window
driver.switch_to.window(base_window)
print(driver.title)
sleep(5)
# Allow access to location
allow_location_btn = driver.find_element(By.XPATH, '//*[@id="c-763985040"]/main/div/div/div/div[3]/button[1]')
allow_location_btn.click()
# "Not interested" for notification
sleep(5)
notification_btn = driver.find_element(By.XPATH, '//*[@id="c-763985040"]/main/div/div/div/div[3]/button[2]')
notification_btn.click()
# Click "I accept" for cookies
sleep(5)
cookies = driver.find_element(By.XPATH, '//*[@id="c964396036"]/div/div[2]/div/div/div[1]/div[1]/button')
cookies.click()

# Tinder free tier only allows 100 "Likes" per day.
actions = ActionChains(driver)
for n in range(100):
    sleep(3)
    try:
        actions.send_keys(Keys.ARROW_RIGHT)
        actions.perform()

    # Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()
        # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(2)
