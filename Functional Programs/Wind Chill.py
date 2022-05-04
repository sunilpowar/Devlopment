import math

t = float(input("Temparature : "))
v = float(input("Wind Speed : "))
w = 35.74 + 0.6215*t + (0.4275*t - 35.75) * (v ** 0.16)
 
if t > 50 and 3 < v < 120:
   print("The wind Chill is ", w)
else:
    print("Enter temperature above 50 and wind speed between 3 to 120")