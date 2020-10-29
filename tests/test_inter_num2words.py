from program.inter_num2words import num_to_words
import pytest

def test_num_to_words() :
    assert num_to_words( 204 ) == "two hundred and four"

#don't think this works due to input command