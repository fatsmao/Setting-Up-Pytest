import pytest
from lib.password_checker import *

"""
Test to check that password will pass if 8 characters or more

class PasswordChecker:
    def check(self, password):
        if len(password) >= 8:
            return True
        else:
            raise Exception("Invalid password, must be 8+ characters.")
"""

def test_password_valid():
    password = PasswordChecker()
    result = password.check("interesting")
    assert result == True

def test_error_is_raised_if_password_invalid():
    password = PasswordChecker()
    with pytest.raises(Exception) as e:
            password.check("sad")
    error_message = str(e.value) 
    assert error_message == "Invalid password, must be 8+ characters."

