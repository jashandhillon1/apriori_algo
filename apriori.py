# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:22:41 2019

@author: jashanpreet singh
"""

#importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#importing the dataset
dataset=pd.read_csv('Market_Basket_Optimisation.csv',header= None)
"""As in the dataset the first row represents the headings but in our case there are no heading so that's why we use header= None"""
"""We are given a dataset we has to use in our model but we can't directly use  this data we had to convert it into a list of list"""
transactions=[]
for i in range(0,7501):
    transactions.append([str(dataset.values[i,j]) for j in range(0,20)])
    
#training apirori on dataset
from apyori import apriori
rules=apriori(transactions,min_support=0.003,min_confidence=0.2,min_lift=3,min_length=2)
"""length here is the connection between two products.we need min. of two products to be connected with each other so min lenght=2"""


#visualising the results
results=list(rules)   