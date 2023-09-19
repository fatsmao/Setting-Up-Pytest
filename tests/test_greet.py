from lib.greet import *

def test_greet():
    greeting = greet("Fatma")
    assert greeting == "Hello, Fatma!"