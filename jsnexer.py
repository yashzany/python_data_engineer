import json

from pandas.io.json import json_normalize
import  pandas as pd

with open('C:\\Users\\YASWANTH\\OneDrive\\Documents\\python\\json\\jsonex.json','r',encoding="utf-8") as f:
    d=json.load(f)
    data = pd.json_normalize(d,record_path='multiMedia')

    #print(p)
    #data1=pd.json_normalize(data['multiMedia'])
    #data.to_csv('C:\\Users\\YASWANTH\\OneDrive\\Documents\\python\\json\\jsonex.csv')
    print(data)