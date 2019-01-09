# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 18:02:28 2018

@author: Harsha
"""
import numpy as np
from sklearn import model_selection,neighbors,svm
import pandas as pd
import pickle,os
from sklearn.utils import shuffle
def trainsvm(sp_id,path):
    os.chdir(path)
   
    with open('cnames.pickle','rb') as f:
        cls=pickle.load(f)
    
    df=pd.read_csv('train2.csv')
    for i in range(len(df)):
        if df['Tag'][i]!=sp_id:
            df['Tag'][i]=-1
    
    df1=df.loc[df['Tag']==sp_id]
    df2=df.loc[df['Tag']==-1]
   
    if (len(df1)/len(df2)) < 0.5:
        l=2*len(df1)
        df2=shuffle(df2)
        df2=df2[:l]
   # print(len(df1),', ',len(df2))
    f=[df1,df2]
    
    df=pd.concat(f)    
    X=np.array(df.drop(['Tag'],1))
    y=np.array(df['Tag'])
    
        
            
    X_train,X_test,y_train,y_test =model_selection.train_test_split(X,y,test_size=0.2)
            
    clf =svm.SVC(gamma='scale',kernel='rbf')
    clf.fit(X_train,y_train)
    #print(sp_id,)
    with open('SVM_'+cls[sp_id]+'.pickle','wb') as f:
        pickle.dump(clf,f)
        
                
   # accuracy=clf.score(X_test,y_test)
   # print("Accuracy = ",accuracy)
    #example_measure=np.array([[-1.2837083524559574,-3.028200590907819,0.8824911063176547,2.332610356920756,-1.7695357462911026,1.8528697596074237,-2.3752282716974604,1.3694426925042193,0.31347448329903693,-0.2932260072954178,0.1589362501251235,0.2623677322354707,-0.006278975410193393,-0.017850613853478477,2.2708491093868344,0.7750002507489159,-0.9759755925764836,-0.5338798972182008,0.5019155366054162,1.0538738995046195,0.06773423773171988,-1.1244833845866555,0.008595289420427022,0.14574304365933183,0.07262947524580682,0.06825188198734675]])
    
   # example_measure=example_measure.reshape(len(example_measure),-1)
    #prediction=clf.predict(example_measure)
    
    
    #print(prediction)
if __name__=="__main__":
    path="C:\\Users\\Ramesh\\Desktop\\College Stuff\\7th Sem stuff\\Project\\Speaker\\Train1\\"
    os.chdir(path)
    with open('cnames.pickle','rb') as f:
        cls=pickle.load(f)
    
    for i in range(1,len(cls)+1):
        trainsvm(int(i),path)
        print(i)
        
    
    
    
            