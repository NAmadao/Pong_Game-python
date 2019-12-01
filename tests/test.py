import unittest

from draw_object import Ball

def test_ball():
    ball = Ball(position=(0, 0), dims=(1, 1), shape="circle")
    assert ball.turtle_object.dx == 0.35