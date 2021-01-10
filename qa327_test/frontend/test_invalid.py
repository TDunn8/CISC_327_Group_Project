import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash


class FrontEndInvalidTest(BaseCase):

    def test_invalid(self, *_):

        self.open(base_url + '/thislinkdoesnotexist')
        not self.assert_no_404_errors