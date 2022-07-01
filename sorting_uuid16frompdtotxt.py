#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 18:25:52 2021

@author: swapnil
"""


import pandas as pd

f = pd.read_csv("16-bit UUID Numbers Document.csv",sep="\t")

# c=0
# f1 = open("16-bit UUID Numbers Document_1.csv","a")
# for i in f:
#     c+=1
#     if((c%2)==0):
#         f1.write("{}".format(i.strip("\n")))
#         print(i)
#     else:
#         f1.write("{}\n".format(i.strip("\n")))
# f1.close()
