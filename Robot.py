#!/usr/bin/env python
# encoding: utf-8

from Brain import Brain
from Trade import Account


class Robot:
    def __init__(self, asset, code=None):
        self.brain = Brain(code)
        self.account = Account(asset, 0)


if __name__ == "__main__":
    robot = Robot(100000)
    print(robot.brain.code)

