# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 12:56:41 2018

@author: student
"""

from python_speech_features import mfcc
from python_speech_features import delta
import scipy.io.wavfile as wav
import math
import os
import numpy as np

def features(path,cls):
    """ path: Path of the folder with  wav files 
        cls is the class number, i.e tag  """
        
    os.chdir(path)
    finalfeat=np.zeros((1,27))
    fnames=[x for x in os.listdir(path) if x[-3:]=="wav"]
    for name in fnames :
        (rate,sig) = wav.read(name)
        fr_l=math.floor(rate*0.025)
        mfcc_feat = mfcc(sig,rate,nfft=fr_l+1)
        d_mfcc_feat = delta(mfcc_feat, 2) 
        feat=np.full((len(d_mfcc_feat),27),cls) # first row is the tag
        feat[:,1:14]=mfcc_feat
        feat[:,14:]=d_mfcc_feat
        try:
            finalfeat=np.vstack([finalfeat,feat])
        except:
            print("Error")
            print(finalfeat.shape,feat.shape)
        finally:
            pass
        #print() 
        
    return finalfeat
