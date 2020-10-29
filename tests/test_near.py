import pytest
from program.easy_near import near

def test_small_is_in_big() :
    assert near( 'train', 'rain' ) == True

def test_small_is_not_in_big() :
    assert near( 'lane', 'plane' ) == False