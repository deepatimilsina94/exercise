import math
print("the equation is: y=x^2+6x+9")
a = 1
b = 6
c = 9
discriminant = b**2-4*a*c
if discriminant >= 0:
    root1=(-b+math.sqrt(discriminant))/(2*a)
    root2=(-b-math.sqrt(discriminant))/(2*a)
    print(f"the roots of the equation are: {root1} and {root2}")
else: 
    print("the equation has no real roots")
