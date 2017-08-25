#!/usr/bin/env python
# encoding: utf-8

import numpy as np
import hashlib as hl
import _pickle as cPickle

from var_dump import var_dump
#from decimal import Decimal

from Stock import StockPool

STOCK_KTYPE = 'D'
TIME_ZONE = ['2015-07-05', '2017-08-14']
MEMORY_FILE = 'xbmemory.bat'

class Brain:
    def __init__(self):
        self.stock = StockPool()
        self.lastFeature = None
        self.lastStInfo = None
        try:
            file = open(MEMORY_FILE, 'rb')
            self.features = cPickle.load(file)
            file.close()
        except (BaseException, FileNotFoundError) as e:
            self.features = {}
        self.cycleFeature = None

    def recordMemory(self):
        file = open(MEMORY_FILE, 'wb')
        cPickle.dump(self.features, file, True)
        file.close()

    def getStockInfo(self, code=None):
        code = self.stock.choiceRandomStock() if not code else code
        st_info = self.stock.getStockInfoDetail(code, STOCK_KTYPE, TIME_ZONE[0], TIME_ZONE[1])
        return np.array(st_info.sort_index()[['high', 'open', 'ma5', 'ma10', 'ma20', 'v_ma5', 'v_ma10', 'v_ma20', 'turnover']])

    def checkFeature(self, st_info):
        '''N W L B S '''
        c_featrue = st_info.copy()
        if self.lastStInfo is not None:
            c_times = [1., 1., 0., 0., 0., 0., 0.] if c_featrue[0] - self.lastStInfo[0] > 0 else [1., 0., 1., 0., 0., 0., 0.]
            if self.lastFeature is not None:
                self.features[self.lastFeature] = self.features[self.lastFeature] + c_times if self.lastFeature in self.features else np.array(c_times, dtype=float)

            c_open  = c_featrue[1] - self.lastStInfo[0]
            c_featrue = c_featrue[1:] - self.lastStInfo[1:]
            c_featrue[0] = c_open
            self.lastFeature = hl.sha1((c_featrue > 0).tostring()).hexdigest()
        self.lastStInfo = st_info.copy()

    def checkIncome(self, price):
        if self.lastStInfo is not None:
            c_rate = (price - self.lastStInfo[0])/self.lastStInfo[0]
            if self.lastFeature is not None:
                if self.cycleFeature is not None:
                    if np.float(self.cycleFeature[1])*c_rate > 0:
                        if self.cycleFeature[0] in self.features:
                            c_a = np.asarray(self.cycleFeature[1:], dtype=float)
                            c_a += [c_rate, 1]
                            self.cycleFeature[1:] = c_a
                    else:
                        if self.cycleFeature[0] in self.features:
                            m_r = np.float(self.cycleFeature[1])
                            c_c = self.features[self.cycleFeature[0]][3:-2]
                            c_c = [max(m_r,c_c[0]), c_c[1]] if m_r > 0 else [c_c[0], min(m_r, c_c[1])]
                            self.features[self.cycleFeature[0]][3:-2] = c_c

                            m_d = np.float(self.cycleFeature[2])
                            c_d = self.features[self.cycleFeature[0]][-2:]
                            c_d = [max(m_d, c_d[0]), c_d[1]] if m_r > 0 else [c_d[0], max(m_d, c_d[1])]
                            self.features[self.cycleFeature[0]][-2:] = c_d

                        self.cycleFeature = np.array([self.lastFeature, c_rate, 0.])
                else:
                    self.cycleFeature = np.array([self.lastFeature, c_rate, 0.])


    def makeDecide(self, st_info):
        if st_info.any():
            price = st_info[0].copy()
            if self.lastStInfo is not None:
                self.checkIncome(price)
            self.checkFeature(st_info)
            if self.lastFeature is not None:
                if self.lastFeature in self.features:
                    fea = self.features[self.lastFeature]
                    _bo = fea[5]/(fea[6] if fea[6]>0 else 1)
                    _qa = (fea[1]/(fea[2] if fea[2] > 0 else 1)) * (fea[3]/(abs(fea[4]) if fea[4] != 0 else 1)) * (_bo if _bo > 0 else 1)
                    return 'B' if _qa>2 else ('S' if _qa < 1 else 'W')
        return 'W'


if __name__ == "__main__":
    brain = Brain()
    st_info = brain.getStockInfo()
    for info in st_info:
        brain.makeDecide(info)
    var_dump(brain.features)
