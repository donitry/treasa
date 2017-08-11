#!/usr/bin/env python
# encoding: utf-8

from Brain import Brain
from Trade import Account


class Robot:
    def __init__(self, asset, code=None):
        self.brain = Brain()
        self.account = Account(asset, 0)

    def thinkAboutTrade(self, st_info):
        if self.account.goods >0:
            if self.brain.makeDecide(st_info, 1):
                self.account.sellTrade(st_info[2])
        else:
            if self.brain.makeDecide(st_info):
                self.account.buyTrade(st_info[2])

    def clearGoods(self, st_info):
        if self.account.goods >0:
            self.account.sellTrade(st_info[2])
        return self.account.money


if __name__ == "__main__":
    robot = Robot(100000)
    trades = 5
    while trades > 0:
        st_info = robot.brain.getStockInfo()
        for i in st_info:
            robot.thinkAboutTrade(i)
        trades -= 1
        print("now asset:------%s-----" % (robot.clearGoods(i)))
        print(robot.brain.t_price.featrue)
        print(robot.brain.t_volum.featrue)


