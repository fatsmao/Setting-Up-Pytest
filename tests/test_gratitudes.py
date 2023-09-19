from lib.gratitudes import *

"""
class Gratitudes:
    def __init__(self):
        self.gratitudes = []

    def add(self, gratitude):
        self.gratitudes.append(gratitude)

    def format(self):
        formatted = "Be grateful for: "
        formatted += ", ".join(self.gratitudes)
        return formatted
"""

"""
Test that Gratitudes will initially be an empty array list
"""

def test_empty_array_list():
    gratitudes = Gratitudes()
    assert gratitudes.format() == "Be grateful for: "

def test_single_gratitude_in_array():
    gratitudes = Gratitudes()
    gratitudes.add("life")
    assert gratitudes.format() == "Be grateful for: life"

def test_adding_three_things_to_the_gratitude_array():
    gratitudes = Gratitudes()
    gratitudes.add("life")
    gratitudes.add("family")
    gratitudes.add("sight")
    assert gratitudes.format() == "Be grateful for: life, family, sight"