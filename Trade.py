#!/usr/bin/env python
# encoding: utf-8

import math
from Account import Account

class Trade:
    def __init__(self):
        self.acc = Account(1000)

    def tax(self, tType, tAmount):
        self.acc.cash -= tAmoun*0.0006 if tType=='B' else tAmount*(0.0036)
        if self.acc.cash < 0:
            self.acc.getLoan()




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
        '''偿还债务'''
        if self.loan >0:
            if self.money - amount >= 0:
                pay = min(amount, self.loan)
                self.money -= pay
                self.loan -= pay

    def interestLoan(self):
        '''获得债务'''
        self.money -= self.loan*0.0005*7
        if self.money < 0:
            self.getLoan(abs(self.money))

    def buyTrade(self, price, amount=0, loan=True):
        if self.money > price*100:
            if self.rate <= 0 and amount == 0:
                amount = math.ceil(self.money/price/100)*100
            elif self.goods <= 0 and amount > 0:
                amount = math.ceil(self.money*self.rate/price/100)*100
        need = price * amount
        need += self.taxTrade('buy', need)
        self.money -= need
        if self.money < 0 and loan:
            loan = self.getLoan(abs(self.money))
            self.money += loan
        self.goods += amount
        #print('b:%s price:%s ------ goods:%s money:%s loan:%s' % (amount, price, self.goods, self.money, self.loan))

    def sellTrade(self, price, amount=0):
        tolAsset = self.money + price*self.goods - self.loan
        postion = price*self.goods/tolAsset
        if postion < self.rate and amount > 0:
            return
        else:
            if amount > 0:
                canRate = postion - self.rate
                canAmount = min(math.floor(tolAsset*canRate/price), amount)
            else:
                canAmount = self.goods

            if canAmount >= 100:
                addMoney = canAmount*price - self.taxTrade('sell', canAmount*price)
                self.money += addMoney
                self.goods -= canAmount
                self.payLoan(addMoney)
                #print('s:%s price:%s ++++++ pos:%s goods:%s tolAsset:%s' % (canAmount, price, postion, self.goods, tolAsset))

