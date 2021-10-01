"""
Работа со страницей авторизации.
"""

from models.auth import AuthData
from pages.page_base import BasePage
from locators.locators_page_login import LocatorsPageLogin


class LoginPage(BasePage):

    def email_input(self):
        return self.find_element(LocatorsPageLogin.LOGIN)

    def password_input(self):
        return self.find_element(LocatorsPageLogin.PASSWORD)

    def login_button(self):
        return self.find_element(LocatorsPageLogin.LOGIN_BUTTON)

    def is_auth(self):

        element = self.find_elements(LocatorsPageLogin.USER_BUTTON)
        if len(element) > 0:
            return True
        return False

    def auth(self, data: AuthData):
        self.fill_element(self.email_input(), data.login)
        self.fill_element(self.password_input(), data.password)
        self.click_element(self.login_button())
