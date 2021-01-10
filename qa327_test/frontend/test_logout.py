import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash


# Moch a sample user
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend'),
    balance=50
)

# Moch some sample tickets
test_tickets = [
    {'name': 't1', 'price': '100', 'seller_email': 'test2_frontend@test.com'}
]

class FrontEndLogoutTest(BaseCase):

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_logout(self, *_):
        
        # login as test_user
        self.open(base_url + '/login')
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "test_frontend")
        self.click('input[type="submit"]')
        
        # open home page
        self.open(base_url)
        # open /logout
        self.open(base_url + '/logout')
        # open home page
        self.open(base_url)

        # message from /login means user is redirected from / to /login
        self.assert_element("#message")
        self.assert_text("Please login", "#message")