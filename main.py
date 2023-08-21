import time
import json
from brain import LinkedinBot
from selenium import webdriver
from interface import perm_var_set


def main():
    try:
        with open("data.json") as json_file:
            data = json.load(json_file)
            user_mail = data.get("gmail", "")
            user_password = data.get("password", "")
            if not user_mail or not user_password:
                perm_var_set()
    except FileNotFoundError:
        perm_var_set()

    with webdriver.Chrome("chromedriver.exe") as driver:
        driver.maximize_window()

        time.sleep(0.1)
        LinkedinBot(driver, user_mail, user_password)


if __name__ == "__main__":
    main()

