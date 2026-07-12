# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 23:35:48 2020

@author: Kevin_Liu
"""

import numpy as np
import pandas as pd
df1 = pd.read_csv("flights.csv")
filter_row = df1['month'].isin([11,12])
df1.sort_values(by=['arr_delay'],ascending=False).head()
