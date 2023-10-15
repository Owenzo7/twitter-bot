'''
# Needed modules for Selenium
'''
# from os import error

from os import error
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# from selenium.webdriver.common.keys import Keys


# The code below helps the browser from closing unexpectedly(This is a must)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
chrome_browser = webdriver.Chrome(options=options)
# --------------------------------------------------->

try:
    chrome_browser.get("https://twitter.com/")
except error:
    print("could not fetch the Url link")


try:
    chrome_browser.maximize_window()
except error:
    print("could not maximize the error")


try:
    googleSignUp_button = chrome_browser.find_element(
        By.CLASS_NAME, "S9gUrf-YoZ4jf")
except error:
    print("could not match the find the Button with a wrong class Name")


assertGoogleButton = "S9gUrf-YoZ4jf" in googleSignUp_button.get_attribute(
    "class")

print(f" options --> {assertGoogleButton}")

try:
    googleSignUp_button.click()
except error:
    print("could not click the button")


time.sleep(100)


# try:
#     username_bar = chrome_browser.find_element(
#         By.XPATH, "//span[3]input[@value name='username']")

#     username_bar.clear()

#     username_bar.send_keys("0xenzo.eth")

# except error:
#     print("Username cannot be found")


# try:
#     password_bar = chrome_browser.find_element(By.XPATH, "//input[1]")

#     password_bar.clear()

#     password_bar.send_keys("Owen5308")

# except error:
#     print("Invalid password")


chrome_browser.quit()
