import pandas as pd
import numpy as np
from PyEMD import EMD
from Visualisation  import Visualisation  # 可视化

"""
pip3 install EMD-signal
"""

##载入时间序列数据
def get_data(path,i):
    data = pd.read_csv(path,usecols=[i])
    data = data.values
    return data


def get_emd(data):
    data_value = data[:,0]
    
    # Extract imfs and residue
    # In case of EMD
    emd = EMD()
    emd.emd(data_value)

    # 获得分量+残余分量
    imfs, res = emd.get_imfs_and_residue()
    return imfs, res 

def plot_imf(data_value,imfs,res):
    t = np.arange(0,len(data_value),1)  # t 表示横轴的取值范围
    vis = Visualisation()
    # 分量可视化
    vis.plot_imfs(imfs=imfs, residue=res, t=t , include_residue=True)
    path = "./emd_imf.png"
    vis.save(path)

    # 频率可视化
    vis.plot_instant_freq(t=t ,imfs=imfs)
    vis.show()
    path = "./emd_instant_freq.png"
    vis.save(path)
    

# 保存分量+残余分量
def save_imf(imfs,res):
    for i  in range(len(imfs)):
        a = imfs[i]
        dataframe = pd.DataFrame({'imf{}'.format(i+1):a})
        dataframe.to_csv(r"imf-%d.csv"%(i+1),index=False,sep=',')
    
    # 保存残余分量
    dataframe = pd.DataFrame(res)
    dataframe.to_csv(r"res.csv",index=False,sep=',') 

def test():
    path = "sample.csv"
    data = get_data(path,0)

    imfs, res  = get_emd(data)

    plot_imf(data,imfs, res)

    save_imf(imfs,res)









if  __name__ =="__main__":
    test()