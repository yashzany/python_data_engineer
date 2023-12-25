import pandas as pd
from pathlib import Path
from pandas import  json_normalize
import  json
#out=pd.read_json('C:\\Users\\YASWANTH\\OneDrive\\Documents\\python\\jsonfile.json')

p = Path(r'C:\\Users\\YASWANTH\\OneDrive\\Documents\\python\\new.json')

with p.open('r', encoding='utf-8') as f:
    data2 = json.loads(f.read())

j=json_normalize(data2['feeds'])
#out1=pd.json_normalize(out)
#k=j,['feeds']
#g=j[['id','title']]
#print(g)
#l=g.rename(columns={'multiMedia.id'})
#j.to_csv('C:\\Users\\YASWANTH\\OneDrive\\Documents\\python\\input\\new.csv')
print(j)