import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

# Mock a sample user

test_user = User(
    email='testlogin@test.com',
    name='test_login',
    password=generate_password_hash('Test_login1')
)

@pytest.mark.usefixtures('server')
class LoginTest(BaseCase):
    @patch('qa327.backend.get_user', return_value=test_user)
    def testR1_1(self, *_):

        #Make sure user is logged out, then login and confirm welcome message
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.assert_element("#message")
        
    def testR1_2(self, *_):

        #Make sure user is logged out, then open login and confirm welcome message says 'Please login'
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.assert_text("Please login", "#message")
      
    @patch('qa327.backend.get_user', return_value=test_user)
    def testR1_3(self, *_):

        #Make sure user is logged out, then open login, type user email and pass, submit and confirm weclome message
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "testlogin@test.com")
        self.type("#password", "Test_login1")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")

    def testR1_4(self, *_):

        #Make sure user is logged out, then open login and confirm email and password elements
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.assert_element("#email")
        self.assert_element("#password")

    def testR1_5(self, *_):

        #Make sure user is logged out, then open login and confirm welcome message says 'Please login'
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.assert_text("Please login", "#message")

    def testR1_6(self, *_):

        #Enter an empty password, then empty username, check for format error
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "testlogin@test.com")
        self.click('input[type="submit"]')
        self.assert_element("#email")
        self.assert_element("#password")
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#password", "Test_login1")
        self.click('input[type="submit"]')
        self.assert_element("#email")
        self.assert_element("#password")

    def testR1_7(self, *_):

        #Enter an invalid email with no '.com;, enter invalid email with no '@', check for format error
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test@test")
        self.type("#password", "Test_login1")
        self.click('input[type="submit"]')
        self.assert_text("Email format error", "#message")
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "testtest.com")
        self.type("#password", "Test_login1")
        self.click('input[type="submit"]')
        self.assert_text("Email format error", "#message")

    def testR1_8(self, *_):

        #Enter invalid passwords with not enough characters, no capital, no lower case, no special symbol, check for format error
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "testlogin@test.com")
        self.type("#password", "T_st1")
        self.click('input[type="submit"]')
        self.assert_text("Email format error", "#message")
        
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test_login@test.com")
        self.type("#password", "test_1")
        self.click('input[type="submit"]')
        self.assert_text("Email format error", "#message")
        
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "testlogin@test.com")
        self.type("#password", "TEST_1")
        self.click('input[type="submit"]')
        self.assert_text("Email format error", "#message")
        
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "testlogin@test.com")
        self.type("#password", "Test11")
        self.click('input[type="submit"]')
        self.assert_text("Email format error", "#message")
    
    def testR1_11(self, *_):

        #Test incorrect email or password, check for error message
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "wrong@email.com")
        self.type("#password", "Test_login1")
        self.click('input[type="submit"]')
        self.assert_text("Email format error", "#message")

        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "testlogin@test.com")
        self.type("#password", "Wrong_pass1")
        self.click('input[type="submit"]')
        self.assert_text("Email format error", "#message")
        

        
