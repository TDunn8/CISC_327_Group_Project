import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash


# Moch a sample user
test_user = User(
    email='testfrontend@test.com',
    name='testfrontend',
    password=generate_password_hash('Test_frontend1!'),
    balance=50
)

# Moch some sample tickets
test_tickets = [
    {'name': 't1', 'quantity': '10', 'price': '100', 'expirationDate':'20210101', 'seller_email': 'test2frontend@test.com'}
]


class FrontEndHomePageTest(BaseCase):

    def test_redirect_login(self, *_):
        self.open(base_url)
        self.assert_element("#message")
        self.assert_text("Please login", "#message")




    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_header(self, *_):

        #login as test_user
        self.open(base_url + '/login')
        self.type("#email", "testfrontend@test.com")
        self.type("#password", "Test_frontend1!")
        self.click('input[type="submit"]')
        
        # open home page
        self.open(base_url)

        # test if header exists
        self.assert_element("#welcome-header")
        self.assert_text("Welcome testfrontend!", "#welcome-header")




    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_balance(self, *_):

        #login as test_user
        self.open(base_url + '/login')
        self.type("#email", "testfrontend@test.com")
        self.type("#password", "Test_frontend1!")
        self.click('input[type="submit"]')
        
        # open home page
        self.open(base_url)

        # test if user balance exists
        self.assert_element("#user-balance")
        self.assert_text("Your balance is 50!", "#user-balance")




    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_logout(self, *_):

        #login as test_user
        self.open(base_url + '/login')
        self.type("#email", "testfrontend@test.com")
        self.type("#password", "Test_frontend1!")
        self.click('input[type="submit"]')
        
        # open home page
        self.open(base_url)

        # test if logout link points to /logout
        self.click('a[href="/logout"]')
        self.assert_element("#message")
        self.assert_text("Please login", "#message")




    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_tickets_available(self, *_):

        #login as test_user
        self.open(base_url + '/login')
        self.type("#email", "testfrontend@test.com")
        self.type("#password", "Test_frontend1!")
        self.click('input[type="submit"]')
        
        # open home page
        self.open(base_url)

        # test if available tickets exists
        self.assert_element("#tickets tr td")
        self.assert_text("t1", "#tickets tr td")




    # R3.9 NEEDS TO BE ADDED
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_sell(self, *_):

        #login as test_user
        self.open(base_url + '/login')
        self.type("#email", "testfrontend@test.com")
        self.type("#password", "Test_frontend1!")
        self.click('input[type="submit"]')
        
        
        # open home page
        self.open(base_url)

        # test sell form exists and works
        self.type("#sell-name", "t2")
        self.type("#sell-quantity", "5")
        self.type("#sell-price", "20")
        self.type("#sell-expirationDate", "20331122")
        self.type("#sell-email", "testfrontend@test.com" )
        self.click('input[id="submit-sell"]')
        # test form is posted to /sell
        # MUST BE COMPLETED WHEN /SELL IS CREATED
        self.assert_element("#sell")
        



    # R3.10 NEEDS TO BE ADDED
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_buy(self, *_):

        #login as test_user
        self.open(base_url + '/login')
        self.type("#email", "testfrontend@test.com")
        self.type("#password", "Test_frontend1!")
        self.click('input[type="submit"]')
        
        
        # open home page
        self.open(base_url)

        # test buy form exists and works
        self.type("#buy-name", "t1")
        self.type("#buy-quantity", "1")
        self.click('input[id="submit-buy"]')
        # test form is posted to /buy
        # MUST BE COMPLETED WHEN /BUY IS CREATED
        self.assert_element("#buy")




    # R3.11 NEEDS TO BE ADDED
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_update(self, *_):

        #login as test_user
        self.open(base_url + '/login')
        self.type("#email", "testfrontend@test.com")
        self.type("#password", "Test_frontend1!")
        self.click('input[type="submit"]')
        
        
        # open home page
        self.open(base_url)


        # test update form exists and works
        self.type("#update-name", "t2")
        self.type("#update-quantity", "4")
        self.type("#update-price", "30")
        self.type("#update-expirationDate", "2033-11-22")
        self.click('input[id="submit-update"]')
        # test form is posted to /update
        # MUST BE COMPLETED WHEN /UPDATE IS CREATED
        self.assert_element("#update")
