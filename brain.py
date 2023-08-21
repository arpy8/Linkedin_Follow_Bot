import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class LinkedinBot:
    def __init__(self, driver, user_mail, user_password):
        self.driver = driver
        self.login(user_mail, user_password)
        self.send_connection_requests()

    def login(self, user_mail, user_password):
        self.driver.get("https://www.linkedin.com/login")
        gmail = self.driver.find_element(By.ID, "username")
        password = self.driver.find_element(By.ID, "password")
        gmail.send_keys(user_mail)
        password.send_keys(user_password)
        password.send_keys(Keys.ENTER)
        self.driver.get("https://www.linkedin.com/mynetwork")
        time.sleep(4)

    def send_connection_requests(self):
        try:
            connect_button = self.driver.find_element(By.XPATH, '//*[@id="ember60"]/li-icon/svg')
            connect_button.click()
        except NoSuchElementException:
            print("Error: Connect button not found")

        time.sleep(5)

        connect_buttons = self.driver.find_elements(By.CSS_SELECTOR, 'li div section div footer .artdeco-button__text')
        for button in connect_buttons:
            try:
                button.click()
                time.sleep(0.05)
                print("Connection request sent successfully.")
            except Exception as e:
                print("Error sending connection request:", e)