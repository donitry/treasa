#!/usr/bin/env python
# encoding: utf-8

import math

class Account:
    def __init__(self, money, rate):
        self.rate = rate
        self.money = money
        self.loan = 0
        self.goods = 0

    def taxTrade(self, ttype, tmoney):
        if ttype == 'sell':
            tax = tmoney*(0.0006+0.003)
        elif ttype == 'buy':
            tax = tmoney*0.0006
        else:
            tax = 0
        return tax

    def getLoan(self, amount):
        self.loan += math.ceil(amount)
        return math.ceil(amount)

    def payLoan(self, amount):
        if self.loan >0:
            if self.money - amount >= 0:
                pay = min(amount, self.loan)
                self.money -= pay
                self.loan -= pay

    def interestLoan(self):
        self.money -= self.loan*0.0005*7
        if self.money < 0:
            self.getLoan(abs(self.money))

    def buyTrade(self, price, amount):
        if self.goods <= 0 and self.money > 0:
            amount = math.ceil(self.money*self.rate/price/100)*100
        need = price * amount
        need += self.taxTrade('buy', need)
        self.money -= need
        if self.money < 0:
            loan = self.getLoan(abs(self.money))
            self.money += loan
        self.goods += amount
        print('buy:%s price:%s ------ goods:%s money:%s loan:%s' % (amount, price, self.goods, self.money, self.loan))

    def sellTrade(self, price, amount):
        tolAsset = self.money + price*self.goods - self.loan
        postion = price*self.goods/tolAsset
        if postion < self.rate and self.rate > 0:
            return
        else:
            canRate = postion - self.rate
            canAmount = min(math.floor(tolAsset*canRate/price), amount)
            if canAmount > 100:
                addMoney = canAmount*price - self.taxTrade('sell', canAmount*price)
                self.money += addMoney
                self.goods -= canAmount
                self.payLoan(addMoney)
                print('sell:%s price:%s ++++++ pos:%s tolAsset:%s' % (canAmount, price, postion, tolAsset))

