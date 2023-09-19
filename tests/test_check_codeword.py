from lib.check_codeword import *

def test_check_codeword():
    password = check_codeword("happy")
    assert password == "WRONG!"
