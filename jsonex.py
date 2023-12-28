import json
import csv
from pandas.io.json import json_normalize
import pandas as pd
import pymysql
from sqlalchemy import create_engine
from xml.etree import ElementTree


#conn= pymysql.connect(host="localhost",user="root",password="tiger",database="sakila")
#conn = create_engine("mysql://root:tiger@localhost/sakila")

#cursor = conn.cursor()

#cursor.execute("truncate table test")

#xml = ElementTree.parse("data.xml")

with open('C:\\Users\\YASWANTH\\OneDrive\\Documents\\python\\jsonfile.json',encoding="utf-8") as f:
    data = json.load(f)
class fff:
    def f11():

            fname = "C:\\Users\\YASWANTH\\OneDrive\\Documents\\python\\file_xml.csv"


            with open(fname, "w",newline='',encoding="utf-8") as file:
                csv_file = csv.writer(file)
                csv_file.writerow(["id", "title","id", "profilePicture", "loca","likes","names"])
                for master in data['feeds']:
                    for master1 in master['multiMedia']:

                     l= csv_file.writerow([master['id'],master['title'],master1['id'],master1['name'], master['profilePicture'], master['location'], master['likeDislike']['likes'],master['name']])
                     print(l)
    def sql11():

        for master in data['feeds']:
            for master1 in master['multiMedia']:
               l=([master['id'], master['title'], master1['id'], master1['name'], master['profilePicture'],
                     master['location'], master['likeDislike']['likes'], master['name']])
               print(l)
               p=pd.DataFrame(l)
               p.to_csv("C:\\Users\\YASWANTH\\OneDrive\\Documents\\python\\file_csv.csv")
               #  cursor.execute(" insert into test values(%s)",(id))
        # conn.commit()
        # conn.close()

    def newj():
        #with open('C:\\Users\\YASWANTH\\OneDrive\\Documents\\python\\jsonex.json',encoding="utf-8") as file1:
         d= json.load(data)
         #df=pd.json_normalize(d,record_path=['feeds'])
         print(d.head())
        #k=f.to_csv("C:\\Users\\YASWANTH\\OneDrive\\Documents\\python\\jso1.csv")
        #print(pd.json_normalize(j))


obj1=fff.newj()
obj1