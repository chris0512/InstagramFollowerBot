from selenium import webdriver
import time

from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH = "C:\\Development\\chromedriver_win32\\chromedriver.exe"
INSTAGRAM_EMAIL = "doe622134@gmail.com"
INSTAGRAM_PASSWORD = "4ea53766"
path = CHROME_DRIVER_PATH
SIMILAR_ACCOUNT = "buzzfeedtasty"


class InstaFollower:

    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(5)

        email = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        password = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')

        time.sleep(3)
        email.send_keys(INSTAGRAM_EMAIL)
        password.send_keys(INSTAGRAM_PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        time.sleep(2)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        time.sleep(2)
        modal = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()



bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()


