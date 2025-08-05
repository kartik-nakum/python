#1) write a program that prints your name and your colege name
name="kartik"
college="atmiya univercity"

print("name:",name)
print("college:",college)

# 2}write a program that prints your address with name, allin new lines

name="kartik"
address="""jamnagar
           rajkot atmiya univercity
           361007"""

print("name:",name)
print("address:\n",address)

# #3) write a program that accept two numbers and perform all basic mathematical operations

a=20
b=10

c=a+b
print(c)
c=a-b
print(c)
c=a*b
print(c)
c=a/b
print(c)
c=a%b
print(c)

# #4) Write a program to calculate simple interest.

p=float(input("enter the principal amount:"))
r=float(input("enter the rate of interst:"))
t=float(input("enter the time period years:"))

interest=(p*r*t)/100
print("simple interest",interest)

# 5) Write a program to calculate 10% bonus of salary.
salary = float(input("Enter your salary: "))

bonus = salary * 0.10

print("The 10% bonus on your salary is:" ,bonus)

# 6) Write a program to convert KM into Meter
km = float(input("Enter the distance in kilometers: "))


meters = km * 1000

print(" kilometers is in to meters.",meters)

#7) The distance between two cities is input through keyboard. Write a program to convert and
#print this distance in feet, meter, inch and centimeter.

km = float(input("Enter the distance between two cities in kilometers: "))

meters = km * 1000      
feet = km * 3280.84     
inches = km * 39370.1  
centimeters = km * 100000 

print("\nThe distance in different units:")
print("Meters:", meters)
print("Feet:", feet )
print("Inches: ",inches)
print("Centimeters:", centimeters)