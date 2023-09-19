from lib.counter import *

def test_counter():
    counter = Counter()
    counter.add(8)
    assert counter.report() == "Counted to 8 so far."
