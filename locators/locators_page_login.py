"""
Уникальные идентификаторы страницы авторизации.
"""

from selenium.webdriver.common.by import By


class LocatorsPageLogin:

    LOGIN = (By.ID, "username")
    LOGIN_BUTTON = (By.ID, "loginbtn")
    PASSWORD = (By.ID, "password")
    USER_BUTTON = (By.CLASS_NAME, "userbutton")