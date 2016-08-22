from ..double import double

def test_double_number():
    assert double(2)==4

def test_double_string():
    assert double("Hello")=="HelloHello"
