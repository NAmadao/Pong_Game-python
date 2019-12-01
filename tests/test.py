import unittest

from players import Player

def player_score_init_test():
    player = Player()
    assert player.score == 0