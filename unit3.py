#unit3

#REGULAR EXPRESSION(RE)
#string=r'm/w/w'
#print(string)

#r:-regular expression, row string
#m:-first character must start with 'm'
#w:-means any alpha numeric character followed by 'm'

# string1='this will be printed on the \n new line'
# print(string1)

# string1=r'this will be printed on the \n new line'
# print(string1)

# #using compile method of re module
import re
abc=re.compile(r'm\w\w')
string1='new day mats matter'
result=abc.search(string1)
print(result.group())

#create  a RE to serach the string that have 'a' at any postion any having total 3 characters
#after it using findall()
import re
string1='atmiya atm sten strnge'
result=re.findall(r'a\w\w',string1)
print(result)

#re.split(r'\w+',string1)
import re
string1='Hello!,Welcome to, the class; Wish you !Good Morning'
result=re.split(r'\W+',string1)
print(result)

#split(), splits the given string into pieces  according to the regular expression and returns the
#pieces as an elements of the list.

#replcaing the sub-treing with the other string
import re
string1='India is the great country'
print(string1)
result=re.sub('India','Bharat',string1)
print(result)

# import re
string1='sun shines sooner or laster s'
# result=re.findall(r's[\w]*',string1)
result=re.findall(r's\w+',string1)
print(result)

#create RE that finds word staring with a number
import re
string1='An lecture is arranged on 26th and 29th of this month'
result=re.findall(r'\d[\w]*',string1)
print(result)

#create RE that retrieve words having 5 characters
import re
string1='Feb Marc April Spetem October'
result=re.findall(r'\b\w{5}\b',string1)
print(result)

#create RE that retrieve words having 5 or 6 characters
import re
string1='Feb Marc April Spetem October'
result=re.findall(r'\b\w{5,6}\b',string1)
print(result)

#create RE that retrieve words having 4 or more characters but not than 6 characters
import re
string1='Feb Marc April Spetem October'
result=re.findall(r'\b\w{4,6}\b',string1)
print(result)

# Create re that retrieves only digits having single digit
import re
string1='one two 3 13'
result=re.findall(r'\b\d\b',string1)
print(result)

#Create re that retrieves the last character of the string which stars with 's'
import re
string1='four five seven'
result=re.findall(r's[\w]*(\w)$',string1)
print(result)

# Create re that retrieves the enrollment number of the student
import re
string1='aaa 123'
result=re.findall(r'\d+',string1)
print(result)

# Create re that retrieves the name of the student
import re
string1='aaa 123'
result=re.findall(r'\D+',string1)
print(result)

# Create re that retrieves word starting with 'st'
import re
string1='strange summer sun student semester'
result=re.findall(r'st[\w]*',string1)
print(result)

# Create re that retrieves word starting with 'st' or 'su'
import re
string1='strange summer sun student semester'
result=re.findall(r's[t,u][\w]*',string1)
print(result)

#Function

#Syntax:
#def name_func(para-1,para2,para3):
#   function statements

# Add two values using function
def sum(a,b):
	total=a+b
	print('the sum of two values is:',total)
# calling the function
sum(2,5)
sum(2.5,5.2)	

# Returning the result from the function
def sum(a,b):
	total=a+b
	return(total)
# calling the function
x=sum(2,5)
print('the sum of two values is:',x)
y=sum(2.5,5.2)
print('the sum of two values is:',y)

# To check whether the number is odd or even using function
def even_odd(no):
	if no%2==0:
		print('the number is even')
	else:
	    print('the number is odd')
# Calling the function
even_odd(2)
even_odd(21)

# To check whether entered number is positive,nagative or zero using function
def pos_neg_zer(no):
	if no>0:
		print('the number is positive')
	elif no==0:
	    print('the number is zero')
	else:
	    print('the number is nagative')    
# Calling the function
n=int(input('enter the number:'))
pos_neg_zer(n)	    


#Returning multiple values from a function
#perfrom basic arithmetic operations using function
def arith(a,b):
	add=a+b
	sub=a-b
	mul=a*b 
	div=a/b 
	return add,sub,mul,div
#calling the function
x,y,z,p=arith(20,5)
print('the addition of two numbers is:',x)
print('the subtraction of two numbers is:',y)
print('the multiplication of two numbers is:',z)
print('the division of two numbers is:',p)	

#pass by object
#immutable object: integer ,string,float,tuple
#mutable object: list
#to pass an integer to a function and modify it
def modify(x):
	x=25
	print('the value of x inside the function is:',x,id(x))
#calling the function
x=52
modify(x)
print('the value of x outside the function is:',x,id(x))

#to pass an list to a function and modify
def modify(lst):
	lst.append(25)
	print('the value of x inside the function is:',lst,id(lst))
#calling the function
lst=[2,5,8,7]
modify(lst)
print('the value of x outside the function is:',lst,id(lst))

#formal and actual arguments
#def sum(a,b): --> formal arguments
# ---
# ---
#calling the function
#s=2,t=5 -->actual arguments

#there four types of actual arguments
# 1. positional arguments
# 2. keyword arguments
# 3. default arguments
# 4. variable length arguments

# 1. positional arguments
# the number arguments and their positions in the function defination shoul match exactly
# with the number and positionsof the argumentsin the function call
def combine(a,b):
	c=a+b 
	print(c)
#calling the function
combine('atmiya','university')	
combine('university','atmiya')	
combine('atmiya','university','rajkot')
combine('atmiya')	

# 2. keyword arguments
# keyword arguments identifies parameters by their names
# while calling the function we have to pass two values
# one is arguments name and teoits values
def stud(roll,name):
    print('the roll number is:',roll)
    print('the name is',name)
# calling the function
stud(roll=1,name='abc')
stud(name='anv',roll=1)  

# 3. default arguments
# it is required if a programerwants to set default value to some parameters
# if at the time of calling function the value is not passed than default value will be taken
# if the value is passed than value passed will be taken  
def stud(roll,name='abc'):
    print('the roll number is:',roll)
    print('the name is',name)
# calling the function
stud(1,'abkk')
stud(2)  

# 4. variable length arguments
#if in case the programmer is unaware about the numberof parameters to be uswd than he can use variable length arguments
# if teo parameters are declared and insert value for three than error will be generated
# format:def name_of_func(farg,*args)
def total(farg,*args):
	sum=0
	for i in args:
		sum=sum+i
	print('the total of all numbers is:',(farg+sum))	
#calling the function
total(10,2)
total(10,2,3,4)	

#passing a group of elements toa function
def disp(abc):
	for i in abc:
		print(i)
#taking a values from the user
print('enter the values')
abc=[a for a in input().split( )]
disp(abc)	

#anonymous function(lambda)
# while using normal funtion we need to define a function and give name to it 
# def name_of_func(a,b):
# while using anonymous function there is no need of giving name to the function
# def sqr(no):
#      return no*no 
# finding the square of a number using lambda

sqr=lambda no:no*no
no=int(input('enter the number:'))
print('the square of the enterd number is :',sqr(no))

#find out the biggest number from two numbers
big=lambda a,b:a if a>b else b 
a,b=3,10
print('the biggest value is:',big(a,b))

#file handling

#creating the file
f=open('ttt.txt','w')
str=input('enter the text:')
f.write(str)
f.close()
#reading the file
f=open('ttt.txt','r')
a=f.read()
print(a)

# checking whether the file is exist or not
# os amd sys are modules
# path is a sub-module of os module
# isfile()is the method of path sub-module
import os,sys
file_name=input('enter the filre:')
if os.path.isfile(file_name):
	f=open(file_name,'r')
else:
	print(file_name+'does not exist')
	sys.exit()
str=f.read()
print(str)
f.close()	

#counting number of lines,characters and words in the file if thefile exist
import os,sys
file_name=input('enter the filre:')
if os.path.isfile(file_name):
	f=open(file_name,'r')
else:
	print(file_name+'does not exist')
	sys.exit()
lc=wc=cc=0
for line in f:
	words=line.split()
	lc=lc+1
	wc=wc+len(words)
	cc=cc+len(line)
print('number of characters in the file are:',cc)
print('number of words in the file are:',wc)
print('number of lines in the file are:',lc)
f.close()

#appending the file
f=open('abc.txt','a')
str_append=',rajkot'
f.write(str_append)
f.close()
f=open('abc.txt','r')
str=f.read()
print(str)
f.close()

#working with the binary files
# program to copy an image file to another file
f1=open('abc.txt','rb')
f2=open('nihal.txt','wb')
bhakti=f1.read()
f2.write(bhakti)
f1.close()
f2.close()

# using with statment
# it will take care of closing an opened file
# format: with open ('file_name','open_mode')as f:
# the seek()and tell methods
# tell:():it is used to know the position of the file pointer
#         it will return the current position of the file position
#         format:n=f.tell()
# seek():it is used to move the file pointer to the position we want pointer to  
#        format: f.seek(offset,fromwhere) 
#        offset:it means number of bytes to move
#        fromwhere:it means from where to move     

# taking the menu item from the user and stroe it in the file restaurant
record_len=15
with open('restaurant.bin','wb')as f:
	no=int(input('enter the numer of food items:'))
	for i in range(no):
		restaurant=input('enter the food items you want tohavein the menu:')
		ln=len(restaurant)
		restaurant=restaurant+(record_len-ln)*' '
		restaurant=restaurant.encode() # it converts text to binary from
		f.write(restaurant)

# take the record number from the use and display the food item at that record number.
record_len=15
with open('restaurant.bin','rb')as f:
	n=int(input('enter the record number:'))
	f.seek(record_len*(n-1))
	str=f.read(record_len)
	print(str.decode())

# zipping the contents of the file
# ZIP_DEFLATED:will compress the data and will be ziped
# Zip_STORED:will just save the data in the zip file
from zipfile import*
f=ZipFile('demo.zip','w',ZIP_DEFLATED)
f.write('restarurant.bin')
f.write('au_logo.png')
f.close()

#unzip
from zipfile import*
f=ZipFile('demo.zip','r')
f.extractall('d:')
f.close()