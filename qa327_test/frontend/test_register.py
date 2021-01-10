import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

# Moch a sample user
test_user = User(
    email='test_frontend@test.com',
    name='name',
    password=generate_password_hash('Testfrontend1!')
)

class test_register(BaseCase):
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R2_1(self, *_):

        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "Testfrontend1!")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")

    def test_R2_2(self, *_):

        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        self.assert_element("#message")
        self.assert_text("Register", "#message")

    def test_R2_3(self, *_):

        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        self.assert_element("#email")
        self.assert_element("#name")
        self.assert_element("#password")
        self.assert_element("#password2")

    def test_R2_4(self, *_):

        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        self.assert_element("#email")
        self.assert_element("#name")
        self.assert_element("#password")
        self.assert_element("#password2")

    def test_R2_5_1(self, *_):

        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        self.type("#name", "newname")
        self.type("#email", "n")
        self.type("#password", "New_password2!")
        self.type("#password2", "New_password2!")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Email format error", "#message")

    def test_R2_5_2(self, *_):

        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        self.type("#name", "newname")
        self.type("#email", "new_emailgmail.com")
        self.type("#password", "New_password1!")
        self.type("#password2", "New_password1!")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Email format error", "#message")

    def test_R2_5_3(self, *_):

        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        self.type("#name", "newname")
        self.type("#email", "new_email@gmail.com")
        self.type("#password", "new_password")
        self.type("#password2", "new_password")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Password is not strong enough", "#message")

    def test_R2_6(self, *_):

        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        self.type("#name", "new_name")
        self.type("#email", "new_email@gmail.com")
        self.type("#password", "New_password")
        self.type("#password2", "New_password2")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("The passwords do not match", "#message")

    def test_R2_7(self, *_):

        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        self.type("#name", " name")
        self.type("#email", "new_email@gmail.com")
        self.type("#password", "New_password2!")
        self.type("#password2", "New_password2!")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Name format error", "#message")
        self.type("#name", "name ")
        self.type("#email", "new_email@gmail.com")
        self.type("#password", "New_password2!")
        self.type("#password2", "New_password2!")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Name format error", "#message")

    def test_R2_8(self, *_):
        
        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        self.type("#name", "ab")
        self.type("#email", "new_email@gmail.com")
        self.type("#password", "New_password2!")
        self.type("#password2", "New_password2!")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Name format error", "#message")
        self.type("#name", "abcdefghijklmnopqrstuvwxyz")
        self.type("#email", "new_email@gmail.com")
        self.type("#password", "New_password2!")
        self.type("#password2", "New_password2!")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Name format error", "#message")

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_R2_9(self, *_):

        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        self.type("#name", "abcd")
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "New_password2!")
        self.type("#password2", "New_password2!")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("User exists", "#message")

    def test_R2_11(self, *_):

        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        self.type("#name", "abcd")
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "New_password2!")
        self.type("#password2", "New_password2!")
        self.click('input[type="submit"]')
        self.open(base_url + '/login')
        self.assert_element("#message")
        self.assert_text("Please login", "#message")
