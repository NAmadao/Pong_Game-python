import unittest

from fml import game_add

def test_game():
    asset = 2
    version = 5
    assert game_add(asset, version) == 7