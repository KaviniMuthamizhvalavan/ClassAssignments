from text_util import TextUtils

obj = TextUtils()

def test_word_count():
    assert obj.word_count("hello world") == 2

def test_unique_words():
    unique = ['hello','world']
    assert obj.unique_words("hello hello world") == unique

def test_reverse_str():
    assert obj.reverse_string("abc") == "cba"

def test_empty():
    assert obj.word_count("") == 0
    assert obj.unique_words("") == []
    assert obj.reverse_string("") == ""

def test_spl_char():
    assert obj.word_count("hello @ world") == 3
    assert obj.unique_words("hello hello @ world") == ['hello', 'world', '@']
    assert obj.reverse_string("hello!") == "!olleh"

def test_case_sensitivity():
    assert obj.word_count("Hello hello") == 1
    assert obj.unique_words("Hello hello") == ['hello']

def test_single():
    assert obj.word_count("hello") == 1
    assert obj.unique_words("Hello") == ['hello']
