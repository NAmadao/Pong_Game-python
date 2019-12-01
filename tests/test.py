import unittest

from players import Player

def player_score_test():
    player = Player()
    assert player.score == 0