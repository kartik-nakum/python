
# #Command line arguments
# The values which are passed as a command line is always stored into the list.
# The name of the list is argv.
# This argv is the part of the sys module.
import sys
print(sys.argv)

# #Program to print the name of python file
import sys
a=sys.argv
print('The name of your python file is: ',a[0])

# #Program to accept two values from the users at the command line and display it.
import sys
a=int(sys.argv[1])
b=int(sys.argv[2])
print('The values are: ',a,b)

# # import sys
a=int(sys.argv[1])
b=int(sys.argv[2])
print('The sum of values are: ',a+b)



# #Check whether the number is positive, negative or zero
a=7
if a==0:
	print('The numnber is zero')
elif a<0:
	print('The number is negative')
else:
	print('The number is positive')

a=int(input('enter the number'))
if a==0:
	print('The numnber is zero')
elif a<0:
	print('The number is negative')
elif a>0:
	print('The number is positive')

# #Discount
bill=int(input('Enter the total bill: '))
if bill<=0:
	print('The bill amount must be more than 0')
elif bill<=999:
	print('You are little bit away to avail a discount')
elif bill>=1000 and bill<=1200:
	print('You will get 10% discount')
elif bill>=1201 and bill<=1500 :
	print('You will get 15% discount')
else: 
	print("Hurray! you availed the maximum discount")

#While
# Allow user to enter as many number they want to until user press 0. 
# Give the sum of all the numbers.
sum=0
num=int(input('Enter a number: '))
while num!=0:
	sum=sum+num
	num=int(input('Enter a num: '))
print('The total of the entered numbers is: ',sum)

# #Print the table of 1.
a=1
ctr=1
print('The table of: ',a)
while ctr<=10:
	ans=a*ctr
	print(a,'x',ctr,'=',ans)
	ctr=ctr+1

# #Display all the even numbers betwee 1-10
n=2
while n>=1 and n<=10:
	print(n)
	n=n+2

#Display all the odd numbers betwee 1-10
n=1
while n>=1 and n<=10:
	print(n)
	n=n+2

# #Display even num or odd num based on users choice (1=odd,2=even)
n=int(input('Enter your choice: '))
if n==1:
	print('You have choosed to print odd numbers between 1-10')
	while n>=1 and n<=10:
		print(n)
		n=n+2
elif n==2:
	print('You have choosed to print even numbers between 1-10')
	while n>=1 and n<=10:
		print(n)
		n=n+2
else:
	print('Enter either 1 or 2')

#Display number and there square
n=1
while(n<=10):
	print(n,'\t',n**2)
	n=n+1

# #Find and display odd numbers from the list
a=[2,7,6,86,43,2,7,9]
b=0
while(b<len(a)):
	if a[b]%2==0:
		print(a[b])
	b=b+1

#Use of len()
a='Welcome to the lab'
print(len(a))

# #Print the characters of the string
a='Rajkot'
b=0
while(b<len(a)):
	print(a[b])
	b=b+1