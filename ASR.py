# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 20:59:04 2018

@author: Harsha
"""

from ASR_KNN import trainsvm
from ASR_fcollect import fcollect
import pickle,os

path="C:\\Users\\Ramesh\\Desktop\\College Stuff\\7th Sem stuff\\Project\\Speaker\\Train1\\"
fcollect(path)
os.chdir(path)
with open('cnames.pickle','rb') as f:
    cls=pickle.load(f)
    
for i in range(1,len(cls)+1):
    trainsvm(int(i),path)
    #print(i)