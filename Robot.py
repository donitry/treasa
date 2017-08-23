#!/usr/bin/env python
# encoding: utf-8

from Brain import Brain
from Trade import Account


class Robot:
    def __init__(self, asset, code=None):
        self.brain = Brain()
        self.account = Account(asset, 0)

    def thinkAboutTrade(self, st_info):
        deci = self.brain.makeDecide(st_info)
        if deci == 'b' and self.account.goods <= 0:
            self.account.buyTrade(st_info[0])
        elif deci == 's' and self.account.goods > 0:
            self.account.sellTrade(st_info[0])


    def clearGoods(self, st_info):
        if self.account.goods >0:
            self.account.sellTrade(st_info[0])
        return self.account.money


if __name__ == "__main__":
    robot = Robot(1000000)
    trades = 3000
    while trades > 0:
        st_info = robot.brain.getStockInfo()
        if not st_info.any():
            continue
        for i in st_info:
            robot.thinkAboutTrade(i)
        trades -= 1
        print("now asset:------%s-----" % (robot.clearGoods(i)))
        if robot.account.money < 50000:
            print('die')
            break
            robot.account.money += 1000000
    robot.brain.recordMemory()






