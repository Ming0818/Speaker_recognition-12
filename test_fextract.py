# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 12:42:34 2018

@author: Harsha
"""

from python_speech_features import mfcc
from python_speech_features import delta
from sklearn import preprocessing
import scipy.io.wavfile as wav
import math
#import os
import numpy as np

def test_features(fname):
    
    #os.chdir(path)
    #feat=np.zeros((1,27))
    #fnames=[x for x in os.listdir(path) if x[-3:]=="wav"]
    (rate,sig) = wav.read(fname)
    #sig=sig[:,1]
    fr_l=math.floor(rate*0.025)
    mfcc_feat = mfcc(sig,rate,nfft=fr_l+1)
    d_mfcc_feat = delta(mfcc_feat, 2) 
    feat=np.zeros((len(d_mfcc_feat),26)) # first row is the tag
    feat[:,:13]=mfcc_feat
    feat[:,13:]=d_mfcc_feat
    
    feat_std=preprocessing.scale(feat)
    
    
    return feat
