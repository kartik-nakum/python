
# unit-2

#Array
# We can declare an array in 3 different ways.
# 1st way
import array
a=array.array('i',[7,9,5,4,6,3])
print(a)

#2nd way
import array as ar
a=ar.array('i',[7,9,5,4,6,3])
print(a)

#3rd way
from array import *
a=array('i',[7,9,5,4,6,3])
print(a)

#Indexing and slicing on arrays
#Indexing
#Using for loop

from array import *
a=array('i',[7,9,5,4,6,3])
print(a)
no=len(a)
# print(no)
for i in range(no):
	print(a[i])

#Using while loop
from array import *
a=array('i',[7,9,5,4,6,3])
print(a)
no=len(a)
# print(no)
i=0
while i<no:
	print(a[i])
	i=i+1

#Indexing of character array

from array import*
character=array('u',['a','b','c','d'])
print(character)
# print(type(character))
for c in character:
	print(c,end=',')

#Slicing
# The format of slicing: array_name[start:stop:stride]

from array import*
a=array('u',['r','a','j','k','o','t','g','u','j','a','r','a','t'])
print(a)
b=a[0:13]
print(b)
b=a[0:]
print(b)
b=a[:13]
print(b)
b=a[-16:]
print(b)
b=a[0:6]
print(b)
b=a[0:13:2]
print(b)
b=a[0::2]
print(b)
b=a[::2]
print(b)

#Slicing using for loop

from array import*
a=array('u',['r','a','j','k','o','t','g','u','j','a','r','a','t'])
# print(a)
for i in a[0:16]:
	print(i,end='')

#Processing the arrays/Array methods
from array import *
a=array('i',[7,9,5,4,6,3])
print(a)
#Appending the values
a.append(2)
print(a)
#Inserting the value
a.insert(0,7)
print(a)
#Removing an element
a.remove(7)
print(a)
#Removing the last element
b=a.pop()
print(b)
#Finding the position of an element
b=a.index(5)
print(b)
#Converting an array to the list
lst=a.tolist()
print(type(a))
print(a)
print(type(lst))
print(lst)

#Accept amount of goods purchased, 
#give the total amount of purchase and the average cost of the product purchased.

from array import*
str=input('Enter the amount: ').split(',')
amount=[int(number)for number in str]
tot_amt=0
for i in amount:
	print(i)
	tot_amt=tot_amt+i
print('The total amount is: ',tot_amt)
l=len(amount)
average=tot_amt/l
print('The average of all the goods is: ', average)

# Indexing and slicing in multi-dimensional array
# Indexing
from numpy import*
a=array([[1,2,3],[4,5,6],[7,8,9]])
# print(a)
for i in range(len(a)):
	print(a[i])
for i in range(len(a)):
	for j in range(len(a[i])):
		print(a[i][j],end='')

# Slicing
from numpy import*
a=array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
print(a[0,:])
print(a[2,:])
print(a[:,0])
print(a[0:1,0:1])
print(a[2,1])

# Creating a new array using the arrays which are already there, based on condition.
# Using where()
# Format: where(condition,expression-1, expression-2) 
from numpy import *
a=array([2,8,13,17,9,16])
b=array([1,9,12,6,15,10])
c=where(b<a,b,a)
print(a)
print(b)
print(c)

#Using nonzero()
#It retrieves the index of the non-zero elemets
from numpy import *
a=array([2,8,0,17,9,16])
c=nonzero(a)
print(type(c))
print(a)
print(c)

#View(), it is also known as 'shallow copying'
#The change/modification in any of the array will be reflected in the other one.

from numpy import *
a=array([2,8,0,17,9,16])
b=a.view()
print(a)
print(b)
a[3]=28
b[4]=82
print(a)
print(b)

#Copy()
from numpy import *
a=array([2,8,0,17,9,16])
b=a.copy()
print(a)
print(b)
a[3]=28
b[4]=82
print(a)
print(b)

#Slicing and Indexing numpyArrays
# from numpy import *
a=array([2,8,0,17,9,16])
print(a)
print(a[:])
print(a[::])
print(a[2:])
print(a[2::2])

#Indexing
from numpy import *
a=array([2,8,0,17,9,16])
print(a)
i=0
while(i<len(a-1)):
	print(a[i])
	i=i+1

#Attributes of an Array
#ndim attribute (it displays 1-single dimensional array, and 2-multidimensional arrary)
from numpy import *
a=array([2,8,0,17,9,16])
print(a)
print(a.ndim)
a=array([[2,8,0],[17,9,16]])
print(a)
print(a.ndim)

#shape attribute (it displays the dimensions of an array)
a=array([2,8,0,17,9,16])
print(a)
print(a.shape)
a=array([[2,8,0],[17,9,16]])
print(a)
print(a.shape)

#size attribute (it displays the number of elements in the array)
a=array([[2,8,0],[17,9,16]])
print(a)
print(a.size)

#dtype (returns the datatype of an array)
a=array([[2,8,0],[17,9,16]])
print(a)
print(a.dtype)
a=array([2,8,0,17,9,16])
print(a)
print(a.dtype)


#Methods of an array
#reshape() method (it converts the array as per the requirement)
#format: array_name.reshape(n,r,c)
a=array([1,2,3,4,5,6,7,8,9,10,11,12])
print(a)
b=a.reshape(2,2,3)
print(a)
print(b)

#flatten() method (it converts the multi-dimensional array to single)
a=array([[1,2,3,4],[5,6,7,8]])
print(a)
# print(a.shape)
b=a.flatten()
print(b)
print(b.shape)


# String Testing Methods

# 1. isalnum()
# 2. isalpha()
# 3. isdigit()
# 4. islower()
# 5. isupper()

# isdigit(): variable_name.isdigit() Condition True/False
UID=input('Enter your AADHAAR No: ')
if UID.isdigit()==False:
	print('Enter valid AADHAAR No.')
else:
	print('Your AADHAAR ID is accepted')

#Allow user to enter strings, in an empty list. Sort the values entered by user and display
string=[]
s=int(input('How many strings you want to enter?: '))
for i in range(s):
	print('Enter the string:', end='')
	string.append(input())
print(string)
string1=string.sort()
for i in string:
	print(i)

#Allow user to enter strings, in an empty list. Check whether the string is available, and at which position?
string=[]
s=int(input('How many strings you want to enter?: '))
for i in range(s):
	print('Enter the string:', end='')
	string.append(input())
#Which string you want to find
temp=False
find=input('Enter the string you want to search: ')
for i in (range(len(string))):
	if find==string[i]:
		print('Your searched string is found at ',i+1,'postion')
		temp=True
if temp==False:
	print('Your searched string is not found.')


# Working with characters
string1='India'
print(string1)
print(type(string1))
character=string1[0]
print(character)
print(type(character))
charcter=string1[4]
print(character)
character=string1[0:3]
print(character)

# Check the type of a character
string1=input('Enter a character: ')
character=string1[0]
if character.isalpha():
	print('User has entered an alphabet.')
	if character.isupper():
		print('The character is in upper case.')
	else:
		print('The character is in lower case.')
else:
	print('User has entered either a number or a special char.')

# Working with List
# Creating list using range
# Format: range(start,stop,stepsize)

# Create a list having numbers from 0-9
list1=range(10)
for i in list1:
	print(i,end='')

list1=range(11,16)
for i in list1:
	print(i,end=' ')

# Store even numbers between 1-10.
list1=range(2,11,2)
for i in list1:
	print(i,end=' ')

# Update the value in the list
#Append
list1=[1,2,3,4,8,7,6,9,60]
list1.append(11)
print(list1)
list1.append(12)
print(list1)
# #Update at the specific location
list1[6]=60
print(list1)
#Deleting the element by value
list1.remove(60)
print(list1)
#Deleting the element by index
del list1[4]
print(list1)
#Finding the length of a string
a=len(list1)
print(a)
#Deleting/Clearing all the elements from the list at a time.
list1.clear()
print(list1)


# Create a list display all the elements in the reverse order.
list1=['Kalawad road', 'Rajkot', 'Guajrat', 'India']
list1.reverse()
print(list1)

#Concatenating two lists.
list1=['Gujarat','Maharashtra','Madhya Pradesh']
list2=['Gandhinagar','Mumbai','Bhopal']
print(list1+list2)

#Printing the same list as many times you want
list1=['Gujarat','Maharashtra','Madhya Pradesh']
print(list1*2)

# Membership 
# Making the use of 'in' and 'not in'
list1=[10,20,30,40,50]
n1=1
n2=30
print(n1 in list1)
print(n1 not in list1)
print(n2 in list1)
print(n2 not in list1)

# We can alias the list
list1=[10,20,30,40,50]
print(list1)
list2=list1
print(list2)
list2[3]=300
print(list2)
print(list1)

#Clone the list
list1=[10,20,30,40,50]
print(list1)
list2=list1[:]
print(list2)
list2[3]=300
print(list2)
print(list1)

#Find how many times an element is available in the list.
list1=[]
num=int(input('How many elements you want to enter?: '))
for i in range(num):
	print('Enter the element: ',end=' ')
	list1.append(int(input()))
print(list1) 
to_find=int(input('Which element you want to find?: '))  
count=0
for i in list1:
	if(to_find==i):
		count=count+1
print('{} is found {} time(s).'.format(to_find,count))

# Finding the common elements
# Converting the list to set
list1=[10,20,30,40,50]
print(list1)
list2=[10,12,30,41,50]
print(list2)
set1=set(list1)
set2=set(list2)
print(set1)
print(set2)
set3=set1.intersection(set2)
print(set3)
print(type(set3))
list3=list(set3)
print(list3)

# wrowking with nested list,accessing the elements.
list=[10,20,30,40,[1,2,3,4]]
print(list)
for i in list[0:4]:
	print(i)
for i in list[4]:
    print(i)	

#working with tuple
tuple1=(10,)
print(tuple1)
print(type(tuple1))   

tuple1=1,2,3,10,20,30
print(tuple1)
print(type(tuple1)) 

list1=[1,2,3,10,20,30]
tuple1=tuple(list1)
print(type(tuple1)) 
print(tuple1)

tuple1=(1,2,3,10,20,30)
a=tuple1[1:3]
print(a) 

tuple1=('abc',1)
name,roll=tuple1[0:2]
print(name)
print(roll)

#function to deal with tuple.
# len,min,max,count,index,sorted.

tuple1=(10,2,30,1,20,3,2)
print(len(tuple1))
print(min(tuple1))
print(max(tuple1))
print(sorted(tuple1))
print(sorted(tuple1,reverse=True))
# print(tuple1.count(3))
print(tuple1.index(1))

#nested tuples
tuple1=(10,2,30,1,(20,3,2))
print(tuple1)
print(tuple1[2])

#take values like roll,name,arks of students,sort it
tuple1=((2,'cde',27),(3,'efg',29),(1,'abc',29),(4,'jkl',19))
print(tuple1)
print(tuple1[2])
print(sorted(tuple1))

#insert a value in the tuple
names=('a','b','c','d','e')
print(names)
nm=input('enter the new name that you want to enter:')
posi=int(input('enter the position at which you want to enter:'))
new_name=tuple(nm)
temp=names[0:posi-1]
print(temp)
temp=temp+new_name
print(temp)
names=temp+names[posi-1:]
print(names)

#modify the value
names=('a','b','c','d','e')
print(names)
nm=input('enter the new name that you want to enter:')
posi=int(input('enter the position at which you want to enter:'))
new_name=tuple(nm)
temp=names[0:posi-1]
print(temp)
temp=temp+new_name
print(temp)
names=temp+names[posi:]
print(names)

#deleting from the specofic position
names=('a','b','c','d','e')
print(names)
posi=int(input('enter the position at which you want to enter:'))
name1=names[0:posi-1]
print(name1)
names=name1+names[posi:]
print(names)


# Dictionary
# Accept number of subjects, and marks from the studen, give the total marks.

marks={}
no=int(input('How many subjects you want to enter?: '))
for i in range(no):
	print('Enter Subject Name: ', end='')
	key=input()
	print('Enter Marks of the subject: ',end='')
	value=int(input())
	marks.update({key:value})
print('The subjects and there marks are: ', marks)
total=sum(marks.values())
print('The total of all entered subjects is: ', total)

# Ask student the name of a subject, display marks of that subject.

name_subject=input('Enter the name of subject: ')
sub_marks=marks.get(name_subject,-1)
if (sub_marks==-1):
	print('Subject not found')
else:
	print('The marks in {} are {}'.format(name_subject,sub_marks))

# Converting lists into dictionary

capital_city=['Bengaluru','Bhopal','Jaipur','Mumbai','Gandhinagar']
state=['Karnataka','MP','Rajasthan','Maharashtra','Guajrat']
a=zip(capital_city,state)
print(a)
state_capital=dict(a)
print(state_capital)
print(type(state_capital))

# zip(): It is used to convert the list or any sequences into a zip class object.
# Converting strings into dictionary

string1='1=abc,2=cde,3=efg,4=hij,5=klm'
print(string1)
lst=[]
for i in string1.split(','):
	a=i.split('=')
	lst.append(a)
print(lst)

dictionary1=dict(lst)
print(dictionary1)

dictionary2={}
for key,value in dictionary1.items():
	dictionary2[int(key)]=value
print(dictionary2)

# Ordered dictionary

from collections import OrderedDict
dict1=OrderedDict()
dict1[1]='A'
dict1[2]='B'
dict1[3]='C'
dict1[4]='D'
print(dict1)
for i,j in dict1.items():
	print(i,j)

# fromkeys()
# Format: dict_name.fromkeys(keys,value)
# keys: Required
# value: optional
d=('a1','a2','a3')
dict1=dict.fromkeys(d)
print(dict1)

d=('a1','a2','a3')
d1=10
dict1=dict.fromkeys(d,d1)
print(dict1)


