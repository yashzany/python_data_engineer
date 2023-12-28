import pandas as pd

dep = pd.read_csv("C:\\Users\\YASWANTH\\OneDrive\\Documents\\python\\input\\dept.csv", index_col=False)

book='jj'
# print(dep)

class school():
    def dep():

        per=pd.read_csv("C:\\Users\\YASWANTH\\OneDrive\\Documents\\python\\input\\per.csv",index_col=False)
        #print(per)

        joinn=pd.merge(dep,per,how='inner',on='id')
        print(type(joinn))
        ##joinn.to_csv("C:\\Users\\YASWANTH\\OneDrive\\Documents\\python\\input\\depper.csv",index=False)
        joinn.to_excel("C:\\Users\\YASWANTH\\OneDrive\\Documents\\python\\input\\depper.xlsx",index=False)

    def sc():
            print(book)

f=school.dep()
f
