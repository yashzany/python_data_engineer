import sqlalchemy as db
import  pandas as pd
from sqlalchemy import create_engine
import numpy as np
import datetime

engine = db.create_engine('mysql+pymysql://root:tiger@localhost:3306/test')

sales=pd.read_csv('C:\\Users\\YASWANTH\\OneDrive\\Documents\\python_pro\\sales.csv',index_col=False)
menu=pd.read_csv('C:\\Users\\YASWANTH\\OneDrive\\Documents\\python_pro\\menu.csv',index_col=False)
#menu.to_sql(name='menu',con=engine,if_exists='replace',index=False)
#print(menu)
menu_sales=pd.merge(sales,menu,on='productid',how='inner')
#menu_sales['year']=menu_sales['order_date'].dt.year
print(type(menu_sales['order_date']))
menu_sales['order_date'] = pd.to_datetime(menu_sales['order_date'], errors='coerce')
j=menu_sales['year']=menu_sales['order_date'].dt.year
d=menu_sales['year']=menu_sales['order_date'].dt.day
price10=menu_sales['price']+100
menu_sales['year']=j
menu_sales['day']=d
menu_sales['price10']=price10
print(menu_sales)
sortv=menu_sales.sort_values(by='location')
#print(f)
f=sortv.groupby(['location','item'])['price'].sum()
#print(f)
#d=f.sort(['location'])
#print(d)
#f.to_csv('C:\\Users\\YASWANTH\\OneDrive\\Documents\\python_pro\\menu-out1.csv')
#sales.to_sql(name='sales',con=engine,if_exists='replace',index=False)
#k=menu_sales['year']=menu_sales['order_date'].dt.year
#menu_sales['Year'] = menu_sales['orderdate'].dt.year


