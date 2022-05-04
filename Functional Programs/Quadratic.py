import math

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
d = b*b - 4*a*c

if d < 0:
    print("This equation ha no any root")
elif d == 0:
    x = (-b + math.sqrt(d))/(2*a)
    print("This equation has one root : ", x)
else:
   x1 = (-b + math.sqrt(d))/(2*a)
   x2 = (-b - math.sqrt(d))/(2*a)
   print("The Roots of equation are", x1 , "and" , x2)