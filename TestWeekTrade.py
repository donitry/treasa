#!/usr/bin/env python
# encoding: utf-8

import numpy as np
#from decimal import Decimal

from Stock import StockPool
from Trade import Account

class Brain:
    def __init__(self, asset, prop, code, ktype):
        self.account = Account(asset, prop)
        self.stock = StockPool()
        if not code:
            code = self.stock.choiceRandomStock()
        self.st_info = self.stock.getStockInfo(code, ktype, '2010-10-01')



if __name__ == '__main__':
    brain = Brain(100000, 0.1, '600276', 'W')
    _list = []
    stArr = np.array(brain.st_info[['open', 'close']])
    for s in stArr:
        #rate = Decimal((s[1]-s[0])/s[0]).quantize(Decimal('0.0000'))
        #close = Decimal(s[1]).quantize(Decimal('0.00'))
        _list.append((s[1]-s[0])/s[0])
        _list.append(s[1])
    raArr = np.array(_list, dtype=np.float).reshape((-1,2))
    for ta in raArr:
        rate = round(ta[0]*100)
        price = round(ta[1],2)
        if rate > 1:
            brain.account.sellTrade(price, rate*100)
        elif rate < -3:
            #amount = round(brain.account.money/price/100)
            #brain.account.buyTrade(price, amount*100)
            brain.account.buyTrade(price, abs(rate)*100)
        #brain.account.payLoan(brain.account.money)
        brain.account.interestLoan()
        #brain.account.money += 1200
    tolAsset = brain.account.goods*price + brain.account.money - brain.account.loan
    print('--tolAsset--', tolAsset, brain.account.goods, brain.account.money, brain.account.loan)


