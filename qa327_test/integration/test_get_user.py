import pytest
from seleniumbase import BaseCase

import qa327.frontend as fn
from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

# Mock a sample user
"""
test_user = User(
    email='testemail@test.com',
    name='testname',
    password=generate_password_hash('Test_pass1')
)
"""
@pytest.mark.usefixtures('server')
class LoginTest(BaseCase):
    
    def test_get_user(self, *_):

        user = fn.bn.get_user("fakeemail@trick.com")
        self.assertEquals(user, None)
        
        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        self.type("#name", "testnam")
        self.type("#email", "testemail@tes.com")
        self.type("#password", "Test_passwod1")
        self.type("#password2", "Test_passwod1")
        self.click('input[type="submit"]')


        user = fn.bn.get_user("testemail@tes.com")
        self.assertEquals(user.name, "testnam")
        
        
