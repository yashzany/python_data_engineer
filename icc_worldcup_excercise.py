import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql://root:tiger@localhost/test")
con = engine.connect()

f=pd.read_csv("C:\\Users\\YASWANTH\\OneDrive\\Documents\\pythonn\\icc_wc_23_bowl.csv")

class iccworld():
    def top5bowlers():



        #k=f.sort_values(by='wickets',ascending=False)
        g= f.groupby('player')['wickets'].sum()
        l=g.sort_values(ascending=False).head(5)
        l.to_csv("C:\\Users\\YASWANTH\\OneDrive\\Documents\\pythonn\\topbowlers.csv")
        #f.to_sql('iccworldcup',con,schema='test',if_exists='append',index=False)
        print(l)

    def top5batsmen():
            t=f.groupby('player')['runs'].sum()
            t=t.sort_values(ascending=False).head(10)
            print(t)
    def avgrun():
            x=int(input('enter avg run rate'))
            #a=f.groupby('player')['run_rate'].mean()
            f1=f.groupby('player')['run_rate'].mean().reset_index()
            #b=a["player"]
            #a.to_csv("C:\\Users\\YASWANTH\\OneDrive\\Documents\\pythonn\\runrate.csv")
            a=f1["run_rate"] < x
            k=f1.where(a).dropna().sort_values(by='run_rate',ascending=True)

            #(a)
            print(k)
    def dynamcicol():
        x=input('enter column name')
        k=f.groupby('player')[x].sum()
        j=k.sort_values(ascending=False).head(5)
        print(j)

f=iccworld.dynamcicol()
f