# Unit Tests for Login Feature
import unittest
from auth_utils import hash_password, verify_password

class TestAuthUtils(unittest.TestCase):
    def test_hash_password(self):
        pwd = 'testpass123'
        hashed = hash_password(pwd)
        assert verify_password(pwd, hashed)
