# 1.  Create a list containing several strings. Take input from the user (search string); display whether 
# entered string is available in the list or not.

string_list = ["apple", "banana", "cherry", "orange", "grape"]
a = input("Enter a the search: ")
if a in string_list:
    print("the string is available in the list")
else:
    print("the NOT available in the list.")


# 2. Accept the string from the user; display the message whether the entered string is palindrome or not
a= input("Enter a string to check if it's a palindrome: ")
if a == a[::-1]:
    print(f"the is a palindrome.")
else:
    print(f"the is NOT a palindrome.")

# 3. Accept the string from the user; display the string in the reverse order
a= input("Enter a string to reverse: ")
reverse = a[::-1]
print("Reversed string:", reverse)


# 4. Accept the string from the user; allow user to choose from the following options and perform 
# the task as per user’s choice. i). Convert to the upper case, ii). Convert to the lower case, iii). 
# Convert to the swap case, iv). Convert to the title case

a = input("Enter a string: ")
print("\nChoose an option:")
print("1. Convert to UPPER case")
print("2. Convert to lower case")
print("3. Convert to Swap Case")
print("4. Convert to Title Case")

choice = input("Enter your choice (1 to 4): ")

if choice == '1':
    print("Upper case:", a.upper())
elif choice == '2':
    print("Lower case:", a.lower())
elif choice == '3':
    print("Swap case:", a.swapcase())
elif choice == '4':
    print("Title case:", a.title())
else:
    print("Invalid choice!")

# 5. Allow users to enter multiple strings in the list; arrange the entered string into alphabetical 
# order and display

slist = []
n = int(input("enter number "))
for i in range(n):

    s = input(f"Enter string {i+1}: ")
    slist.append(s)

slist.sort()
print("\nStrings in alphabetical order:")
for item in slist:
    print(item)

# 6. Create a tuple and display it. Enter 25 at the third position and display it again.
my_tuple=(10,20,30,40,50)
print("orignal tuple:",my_tuple)
temp_list=list(my_tuple)
temp_list.insert(2,25)
my_tuple=tuple(temp_list)
print("update tuple",my_tuple)

# 7. Create a dictionary named library with following keys (Bookid, Title, Author, Price, Publisher).
# a. Display the dictionary, b. Display the name of Author, c. Display the Bookid
# d. Display the length of the dictionary, e. Update the price, f. Insert year as the new key 
# and display the dictionary again.

library = {
    'Bookid': 101,
    'Title': 'Python Programming',
    'Author': 'John Doe',
    'Price': 29.99,
    'Publisher': 'TechBooks Publishing'
}

# a.
print("Dictionary:", library)

# b.
print("Author:", library['Author'])

# c.
print("Bookid:", library['Bookid'])

# d.
print("Length of the dictionary:", len(library))

# e.
library['Price'] = 20
print("Updated Dictionary with new Price:", library)

# f. 
library['Year'] = 2025
print("Dictionary after inserting Year:", library)


# 8. Create a numeric array and perform following operations on it: Add 2 to each elements, 
# Subtract 3 from each element, Multiply each element with 3, Divide each element by 2, Find 
# max and min, find the average of all elements.

import numpy as np
a = np.array([10, 20, 30, 40, 50])
print(a)
print('add' , a + 2)
print('sub' , a - 3)
print('multi' , a * 3)
print('div' , a / 2)

print('Maximum value:',max(a))
print('Minimum value:',min(a))
print('average value:',mean(a))



