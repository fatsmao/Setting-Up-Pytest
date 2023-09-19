from lib.string_builder import *

def test_string_builer_gives_an_empty_string():
    string_builder = StringBuilder()
    assert string_builder.output() == ""

def test_string_builder_will_give_me_a_single_string():
    string_builder = StringBuilder()
    string_builder.add("hello")
    assert string_builder.output() == "hello"


