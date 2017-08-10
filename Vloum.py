#!/usr/bin/env python
# encoding: utf-8

import numpy as np

from Stock import StockPool
from Trade import Account

stock = StockPool()
code = stock.choiceRandomStock()

st_info = stock.getStockInfo(code, 'W', start='2014-01-01')

print(st_info)
