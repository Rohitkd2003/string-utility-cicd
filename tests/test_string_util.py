from src.string_utils import reverse_string,to_lower,to_upper,count_vowels
def test_reverse_string():
    assert reverse_string("abc")=="cba"

def test_to_upper():
    assert reverse_string("hello")=="HELLO"

def test_to_lower():
    assert reverse_string("HELLO")=="hello"

def test_count_vowels():
    assert count_vowels("hello")==2
    assert count_vowels("AEIOU")==5
