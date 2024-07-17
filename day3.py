age = 30
height = 5.1
complex = 1 + 2j
base = float(input("enter base:"))
height = float(input("enter height:"))
area = 0.5 * base * height
print("area of traingle:", area)
length = float(input("enter length of rectangle:"))
width = float(input("enter width of the rectangle:"))
area_r = length * width
perimeter = 2 * (length + width)
print ("area of rectangle:" , area_r)
print("perimeter of rectangle:", perimeter)
radius = float(input ("radius of circle:"))
import math
area_c = math.pi * radius * radius 
print("area of circle:", area_c)
circum = 2 * math.pi * radius
print("circumference of circle:", circum)
x1, y1 = 2, 2
x2, y2 = 6, 10
slope = (y2 -y1) / (x2 - x1)
print ("slope of line:", slope)
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print ("elucidean distance:", distance)
print ("enter your an equation")
xinter = float(input ("enter a value"))
slope = float(input ("enter m"))
yinte = float(input ("enter c"))
slope = float (xinter/slope)
print(slope)
xint = float(slope/yinte)


