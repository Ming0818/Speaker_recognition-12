# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 20:56:23 2018

@author: Harsha
"""

import os,csv,pickle
from mfcc_feat import features
import numpy as np
from sklearn import preprocessing

def fcollect(path):
    
    #path="C:\\Users\\Ramesh\\Desktop\\College Stuff\\7th Sem stuff\\Project\\Speaker\\Train1\\"
    folders=[x for x in os.listdir(path) if '.' not in x]
    tg=['Tag','M0','M1','M2','M3','M4','M5','M6','M7','M8','M9','M10','M11','M12','M13','M14','M15','M16','M17','M18','M19','M20','M21','M22','M23','M24','M25']
    cls=1.0
    feat_write=np.zeros((1,27))
    clas={}
    for x in folders:
        p1=path+x+"\\"
        clas[int(cls)]=x
        temp=features(p1,cls)
        
        feat_write=np.vstack([feat_write,temp[1:,:]])
        cls=cls+1
    feat_write=feat_write[1:,:]
#    feat_std= np.zeros_like(feat_write)
#    feat_std[:,0]=feat_write[:,0]
#    feat_std[:,1:]=preprocessing.scale(feat_write[:,1:])
#    
#    feat_norm=np.zeros_like(feat_write)
#    feat_norm[:,0]=feat_write[:,0]
#    feat_norm[:,1:]=preprocessing.normalize(feat_write[:,1:])
    with open(path+'train2.csv','w',newline='') as f: 
        wr=csv.writer(f)
        wr.writerow(tg)
        wr.writerows(feat_write)
#    with open(path+'train2_standardized.csv','w',newline='') as f:
#        wr=csv.writer(f)
#        wr.writerow(tg)
#        wr.writerows(feat_std)
    with open(path+'cnames.pickle','wb') as f:
        pickle.dump(clas,f)
#with open('train1_norm.csv','w',newline='') as f:
#    wr=csv.writer(f)
#    wr.writerows(feat_norm)    
    
    
    
    

