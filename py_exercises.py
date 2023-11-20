
class ex():
    def multiplication():
     x=int(input('enter first number'))
     print('first number is',x)

     y = int(input('enter second number'))
     print('first number is', y)

     mul=x*y
     print(mul)

    def sepp():
        print('yash','is','smart')
    def decimaltopoint2():
        n=12.2345
        print('%.2f' % n)

    def loo10():
        i=1
        while i <=10:
            print(i)
            i+=1

    def sum():
        x=int(input('enter number'))
        y=0
        for i in range(1,x+1):
             y=i+y
        print(y)

    def mulofgivennum():
        x = int(input('enter number'))
        #y = 2
        for i in range(1, 11):

            print(i*x)
    def cunt():
        x=1234
        print(len(x))

    def primee():
       for i in range(1,10):
            if (i%i)==0:
             print(i)

f=ex.primee()
f