a=int(input("a: "))
b=int(input("b: "))
print(a+b)
if (a+b)%2==0:
    print("even no")
else :
    print("odd no")
    # with out using modules %

a=int(input("a: "))
b=int(input("b: "))
print(a+b)
if ((a+b)//2)*2==0:
    print("even no")
else :
    print("odd no")



a=int(input("sub 1: "))
b=int(input("sub 2: "))
c=int(input("sub 3: "))
d=int(input("sub 4: "))
e=int(input("sub 5: "))
f=(a+b+c+d+e)
print(f)
if f>=300 :
    print("pass")
else:
    print("fail")

a=int(input("enter the value 0 to 500 : "))
print(a)
if (a>=350) :
   print("your pass")
else:
   print("your fail")
 



a=int(input("enter the value of a: "))
b=int(input("enter the value of b: "))

if a is b :
    print("equal")
else:
    print("not equal")

a=int(input("enter the value of a : "))
b=int(input("enter the value of b : "))
c=a<<b
d=a>>b
print(c)
print(d)
if (c>d):
        print(" c is big value")
else:
        print("d is big value")    