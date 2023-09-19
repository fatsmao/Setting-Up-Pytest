import pytest
from lib.present import *

"""
When we wrap an item
We get it back when unwrapping
"""

def test_we_get_an_item_back_if_wrapped():
    contents = Present()
    contents.wrap(3)
    assert contents.unwrap() == 3

""""
If we unwrap before wrapping
We get an error message
"""

def test_if_content_is_wrapped_without_unwrapping():
    contents = Present()
    with pytest.raises(Exception) as e: 
        contents.unwrap()
    error_message = str(e.value) 
    assert error_message == "No contents have been wrapped."
    
    

def test_for_something_already_wrapped():
    contents = Present()
    contents.wrap(5)
    with pytest.raises(Exception) as e:
        contents.wrap(8)
    error_message = str(e.value) 
    assert error_message == "A contents has already been wrapped."