import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import csv
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier,AdaBoostClassifier
from sklearn.metrics import roc_curve,plot_roc_curve,RocCurveDisplay,auc
from utils import csvreader,csvwriter


pd.set_option("display.precision", 16)

if __name__ == "__main__":
    
    rows,fields = read_csv('final_dataset.csv')
    df_m = pd.DataFrame(rows,columns=fields)
    
    df = df_m.drop(columns=['p_g_x','p_g_y','p_g_z','s_g_x','s_g_y','s_g_z'])
    
    df.loc[df[df['attackerType']!='0'].index,'attackerType']='1'
    df.loc[df[df['attackerType']=='0'].index,'attackerType']='0'
    
    y = df['attackerType']
    X = df.iloc[:,:6]
    
    ss = StandardScaler()
    X = ss.fit_transform(X)
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)
    
    
    # DecisionTreeClassifier
    
    tree = DecisionTreeClassifier()
    tree = tree.fit(X_train,y_train)
    
    tree_train_accuracy = tree.score(X_train,y_train)
    tree_test_accuracy = tree.score(X_test,y_test)
    tree_depth = tree.get_depth()
    
    # RandomForestClassifier
    
    rf = RandomForestClassifier()
    rf_train_accuracy = rf.fit(X_train,y_train)
    
    rf_train_accuracy = rf.score(X_train,y_train)
    rf_test_accuracy = rf.score(X_test,y_test)
    
    #AdaBoostClassifier
    
    ada = AdaBoostClassifier()
    ada.fit(X_train,y_train)
    
    rf_train_accuracy = ada.score(X_train,y_train)
    rf_test_accuracy = ada.score(X_test,y_test)