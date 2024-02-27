from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome("C:/selenium/chromedriver.exe")
browser.get("https://www.instagram.com/")
time.sleep(4)

#login
def login():
    username = browser.find_element_by_xpath("""//*[@id="loginForm"]/div/div[1]/div/label/input""")
    username.send_keys("abc_user_name")
    password = browser.find_element_by_xpath("""//*[@id="loginForm"]/div/div[2]/div/label/input""")
    password.send_keys("1234*****")
    password.submit()
    time.sleep(3)
login()

# block notification
def notification():
    notnow = browser.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div").click()
    time.sleep(2)
    noti = browser.find_element_by_xpath("/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]").click()
    time.sleep(1)
notification()

#click msg icon
def massage():
    msgclick = browser.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div/div[5]/div/div/div/span/div/a").click()
    time.sleep(1)
massage()

#send massage
def send_massage():
    src = browser.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div[4]/div").click()
    time.sleep(1)
    friend_name = browser.find_element_by_xpath("/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/input")
    friend_name.send_keys("pure_artistic_day")
    time.sleep(2)
    browser.find_element_by_xpath("/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/div/div[1]").click()
    time.sleep(2)
    browser.find_element_by_xpath("/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[4]/div").click()
    time.sleep(2)
    for i in range(0,5):
        msg = browser.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]")
        msg.send_keys("hello")
        time.sleep(0.5)
        msg.send_keys(Keys.ENTER)
        time.sleep(1)
send_massage()
