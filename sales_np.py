import  numpy as np
import  pandas as pd

sales=pd.read_csv('C:\\Users\\YASWANTH\\OneDrive\\Documents\\python_pro\\sales.csv',index_col=False)
menu=pd.read_csv('C:\\Users\\YASWANTH\\OneDrive\\Documents\\python_pro\\menu.csv',index_col=False)

#print(menu)

menu_sales=pd.merge(sales,menu,on='productid',how='inner')
j=sales.join(menu,how='inner',lsuffix='productid')
g=np.sum(menu_sales)
print(g)