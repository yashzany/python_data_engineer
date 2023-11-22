import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql://root:tiger@localhost/test")
con = engine.connect()

class iccworld():
    def top5bowlers():

        f=pd.read_csv("C:\\Users\\YASWANTH\\OneDrive\\Documents\\pythonn\\icc_wc_23_bowl.csv")

        #k=f.sort_values(by='wickets',ascending=False)
        g= f.groupby('player')['wickets'].sum()
        l=g.sort_values(ascending=False).head(5)
        l.to_csv("C:\\Users\\YASWANTH\\OneDrive\\Documents\\pythonn\\topbowlers.csv")
        #f.to_sql('iccworldcup',con,schema='test',if_exists='append',index=False)
        print(l)

f=iccworld.top5bowlers()
f