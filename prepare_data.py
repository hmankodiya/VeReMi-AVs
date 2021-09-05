import pandas as pd
import numpy as np
import os
import glob
from utils import write_csv,read_csv

def preprocess(gt,df_lf):
    df_gt = gt
    df_gt = df_gt.drop(columns = ['time','type','pos_noise','spd_noise'])
    
    lf_t3 = df_lf[df_lf['type']==3] 
    lf_t3 = lf_t3.drop(columns=['rcvTime','type','sendTime','noise','spd_noise','pos_noise','RSSI'])
    
    merged_t3 = pd.merge(lf_t3, df_gt, on = "messageID")
    prim_X = merged_t3.drop(columns = ['sender_x','sender_y','messageID']) 
    
    px = pd.DataFrame(prim_X["pos_x"].to_list(), columns=['p_l_x', 'p_l_y','p_l_z'])
    sx = pd.DataFrame(prim_X["spd_x"].to_list(), columns=['s_l_x', 's_l_y','s_l_z'])
    py = pd.DataFrame(prim_X["pos_y"].to_list(), columns=['p_g_x', 'p_g_y','p_g_z'])
    sy = pd.DataFrame(prim_X["spd_y"].to_list(), columns=['s_g_x', 's_g_y','s_g_z'])
    at = pd.DataFrame(prim_X["attackerType"], columns=['attackerType'])
        
    cnct = pd.concat([px,sx,py,sy,at],axis=1)
    
    return cnct

def get_files(dir_path='results/'):
    files = glob.glob(dir_path+'*.json')
    df = pd.read_json(files[1],lines=True)
    gt = pd.read_json(files[0],lines=True)
    for i in range(2,len(files)):
        temp = pd.read_json(files[i],lines=True)
        df = df.append(temp)
    return df,gt

def get_from_folder(base_path,folder_path = 'work/ul/ul_vertsys/ul_wqy57/'):
    path = os.path.join(base_path,folder_path)
    folders = os.listdir(path)
    
    X = pd.DataFrame()
    j=1
    for i in folders:
        folder_sims = os.path.join(path,i+'/veins-maat/simulations/securecomm2018/results/')
        print(folder_sims)
        fls,gt = get_files(folder_sims)
        temp = preprocess(gt,fls)
        X = X.append(temp)
        
    return X

if __name__=='__main__':
    X = get_from_folder('D:/PYTHON/Notes/Research-Notes/')
    X = X.drop_duplicates()
    
    fields = X.columns
    final_l =  X.values.tolist()
    
    write_csv(fields,final_l)