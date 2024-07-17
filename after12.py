length_python=len("python")
length_dragon=len("dragon")
print(f"length:{length_python} and {length_dragon}")
# Strings to check
string1 = 'python'
string2 = 'dragon'

# Check if 'on' is in both strings using the and operator
is_in_both = ('on' in string1) and ('on' in string2)

# Print the result
print(is_in_both)

hour = float(input("enter hours:"))
rate_hour = float(input("enter rate per hour"))
pay = hour*rate_hour
print("pay of the person", pay)


years = int(input("enter number of years:"))
life_sec = years*365*24*60*60
print("life in seconds:", life_sec)