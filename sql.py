import  pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql://root:tiger@localhost/test").connect()
con = engine.connect()

f=pd.read_sql('emp1',con)

print(f)