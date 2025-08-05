

def sum_numbers(*args):
    total = sum(args)
    print("Sum:", total)

sum_numbers(10, 20, 30)

# 2. Ask user to enter an integer number, display the table of that number using for loop.


number = int(input("Enter an integer: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# 3. Take a list, store names of five states, take another list store capital of those states.
# Convert the lists into dictionary.

states = ["California", "Texas", "Florida", "New York", "Illinois"]
capitals = ["Sacramento", "Austin", "Tallahassee", "Albany", "Springfield"]

state_capital_dict = dict(zip(states, capitals))
print(state_capital_dict)

# 4. Take voting of five cities in an array, display its total, and average.

voting = [1200, 950, 1350, 1100, 980]
total_votes = sum(voting)
average_votes = total_votes / len(voting)

print("Total Votes:", total_votes)
print("Average Votes:", average_votes)

# 5. Create an image file copy and create the other file.
def copy_image_file(source_path, destination_path):
    with open(source_path, "rb") as src, open(destination_path, "wb") as dest:
        dest.write(src.read())

# Example usage
# copy_image_file("source_image.jpg", "copied_image.jpg")

# 6. Create the Regular Expressions to fulfill following instructions:
# i). that splits the string where one or more non-alphanumeric is found.
# ii). that retrieve the words having 5 or more-character length.
# iii). to retrieve only single digits from a string.


import re

text = "Hello! This, is a test@string with 12345 and some digits like 7, 8, and 9."

# i) Split on non-alphanumeric characters
split_text = re.split(r'\W+', text)
print("Split:", split_text)

# ii) Words with 5 or more characters
long_words = re.findall(r'\b\w{5,}\b', text)
print("Words with 5+ chars:", long_words)

# iii) Only single digits
digits = re.findall(r'\b\d\b', text)
print("Single digits:", digits)

# 7. Create a Bar chart that demonstrates the voting of five states. Data input is to be
# taken in the form of tuple

import matplotlib.pyplot as plt

data = (("California", 1200), ("Texas", 950), ("Florida", 1350), ("New York", 1100), ("Illinois", 980))
states, votes = zip(*data)

plt.bar(states, votes)
plt.title("Voting of Five States")
plt.xlabel("States")
plt.ylabel("Votes")
plt.show()

# 8. Create a Pie chart that demonstrates the voting of five states.
import matplotlib.pyplot as plt

data = (("California", 1200), ("Texas", 950), ("Florida", 1350), ("New York", 1100), ("Illinois", 980))
states, votes = zip(*data)

plt.pie(votes, labels=states, autopct='%1.1f%%', startangle=140)
plt.title("Voting Distribution by State")
plt.axis('equal')
plt.show()


# set B


# 1. Accept two numeric values from the user. Create a function that displays all the
# basic arithmetic operations.
def arithmetic_operations(a, b):
    print(f"Addition: {a + b}")
    print(f"Subtraction: {a - b}")
    print(f"Multiplication: {a * b}")
    if b != 0:
        print(f"Division: {a / b}")
        print(f"Modulus: {a % b}")
    else:
        print("Division and modulus by zero is not allowed.")

# User input
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
arithmetic_operations(x, y)

# 2. Ask user to enter an integer number, display the table of that number using while
# loop
num = int(input("Enter an integer: "))
i = 1
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1
# 3. Take a string, write state name and its capital, convert the sting into dictionary. 

input_str = "California:Sacramento, Texas:Austin, Florida:Tallahassee"
state_dict = dict(item.split(":") for item in input_str.split(", "))
print(state_dict)

# 4. Take marks of five subjects in an array, display its total, and average

marks = [int(input(f"Enter marks for subject {i+1}: ")) for i in range(5)]
total = sum(marks)
average = total / len(marks)

print("Total Marks:", total)
print("Average Marks:", average)

# 5. Create the file ask user to enter the data and display it.
filename = "user_data.txt"
data = input("Enter data to write in the file: ")

with open(filename, "w") as f:
    f.write(data)

with open(filename, "r") as f:
    content = f.read()
    print("File Content:")
    print(content)

# 6. Create the Regular Expressions to fulfill the following instructions:
# i). to find the words starting with a number
# ii). that retrieve the words having 5-character length
# iii). that replaces a string with the new string

import re
text = "1apple banana 234car 12bus apple pie hello world tiger lion 3monkey"

# i) Words starting with a number
start_with_digit = re.findall(r'\b\d\w*', text)
print("Words starting with a number:", start_with_digit)

# ii) Words with exactly 5 characters
five_char_words = re.findall(r'\b\w{5}\b', text)
print("Five-character words:", five_char_words)

# iii) Replace "apple" with "orange"
replaced_text = re.sub(r'apple', 'orange', text)
print("After replacement:", replaced_text)

# 7. Create a Bar chart that demonstrates the voting of five states. Data input is to be
# taken in the form of dictionary.

import matplotlib.pyplot as plt

voting_data = {
    "California": 1200,
    "Texas": 950,
    "Florida": 1350,
    "New York": 1100,
    "Illinois": 980
}

states = list(voting_data.keys())
votes = list(voting_data.values())

plt.bar(states, votes, color='skyblue')
plt.title("Voting of Five States")
plt.xlabel("States")
plt.ylabel("Votes")
plt.show()

# 8. Create a Line chart by assuming the data

import matplotlib.pyplot as plt

years = [2020, 2021, 2022, 2023, 2024]
values = [150, 180, 200, 220, 210]

plt.plot(years, values, marker='o', linestyle='-', color='green')
plt.title("Trend Over Years")
plt.xlabel("Year")
plt.ylabel("Value")
plt.grid(True)
plt.show()


# set-c
# 1. Accept the string from the user; display the message whether the entered string is
# palindrome or not

string = input("Enter a string: ")
if string == string[::-1]:
    print("The entered string is a palindrome.")
else:
    print("The entered string is not a palindrome.")

# 2. Take two arrays and enter 5 digits in both arrays. Compare the corresponding
# element from each array and display only the bigger number.

array1 = [int(input(f"Enter element {i+1} for array1: ")) for i in range(5)]
array2 = [int(input(f"Enter element {i+1} for array2: ")) for i in range(5)]

bigger = [max(a1, a2) for a1, a2 in zip(array1, array2)]
print("Bigger elements from both arrays:", bigger)

# 3. Create the Regular Expressions to fulfill the following instructions:
# i). that retrieve the words having 5 or more-character length.
# ii). that replaces a string with the new string

import re
text = "apple orange watermelon banana kiwi mango peach"

# i) Words with 5 or more characters
long_words = re.findall(r'\b\w{5,}\b', text)
print("Words with 5 or more characters:", long_words)

# ii) Replace string
replaced_text = re.sub(r'banana', 'grape', text)
print("After replacement:", replaced_text)

# 4. A tuition class owner wants to make a simple application to allocate grades to the
# students based on marks student have scored. Accept marks from the students.
# Marks more than 90 – A1 grade, Marks 80 or less than or equal 90 – A grade, Marks
# 70 or less than or equal 80 – B1, Marks 60 or less than or equal 70 – B Marks, 50 or
# less than or equal 60 – Can do Better! Marks < 50 – Need to work hard.


marks = int(input("Enter student marks: "))

if marks > 90:
    grade = "A1 grade"
elif marks > 80:
    grade = "A grade"
elif marks > 70:
    grade = "B1 grade"
elif marks > 60:
    grade = "B grade"
elif marks > 50:
    grade = "Can do Better!"
else:
    grade = "Need to work hard."

print("Student Grade:", grade)

# 5. Create a function that has two parameters enrolment and name. When calling the
# function if the name is not passed, then by default ‘ABC’ must be taken. Store this
# value in the file and display it

def store_student_data(enrolment, name="ABC"):
    data = f"Enrolment: {enrolment}, Name: {name}\n"
    with open("student_data.txt", "a") as file:
        file.write(data)
    print("Data stored in file.")

# Example call
store_student_data("EN12345")
store_student_data("EN12346", "John")

# Display stored data
with open("student_data.txt", "r") as file:
    print("\nStored Data:")
    print(file.read())


# 6. Create an image file copy and create the other file. Zip both files and unzip it.

import shutil
import zipfile
import os

# Copy image
shutil.copy("source.jpg", "copy.jpg")

# Zip both files
with zipfile.ZipFile("images.zip", "w") as zipf:
    zipf.write("source.jpg")
    zipf.write("copy.jpg")

# Unzip
with zipfile.ZipFile("images.zip", "r") as zipf:
    zipf.extractall("unzipped_images")

print("Image copied, zipped, and unzipped successfully.")

# 7. Create a pie chart that demonstrates admissions of five programs. Data input is to
# be taken from the excel file. Program name: MCA, BCA, BSCIT, BCAIIP, MSCIT

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel("admissions.xlsx")  
plt.pie(df['Admissions'], labels=df['Program'], autopct='%1.1f%%', startangle=140)
plt.title("Admissions of Five Programs")
plt.axis("equal")
plt.show()



# set -D

# 1. Create a function to calculate simple interest. Accept amount from the user
def calculate_simple_interest(principal, rate=5.0, time=1):
    si = (principal * rate * time) / 100
    return si

amount = float(input("Enter the principal amount: "))
interest = calculate_simple_interest(amount)
print(f"Simple Interest: {interest}")

# 2. Create an array in such a way that modifying in one array affects the other array and
# vice versa
import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = arr1  # Shared reference

arr2[0] = 100
print("Array 1:", arr1)
print("Array 2:", arr2)

# Both arrays reflect the change because they point to the same object.

# 3. Rajkot Corporation wants to make simple application to calculate the Water Bill of
# Rajkotians. Water is being delivered by the Corporation on per litre charges as
# below: Upto 90 litres – Rs. 0/ltr, Upto 150 litres – Rs. 2/ltr, Upto 250 litres – Rs.
# 5/ltr, more than 250 litres – Rs. 10/ltr, accept unit consumption from consumers and
# display the bill amount

litres = int(input("Enter the amount of water consumed in litres: "))

if litres <= 90:
    bill = 0
elif litres <= 150:
    bill = (litres - 90) * 2
elif litres <= 250:
    bill = (60 * 2) + (litres - 150) * 5
else:
    bill = (60 * 2) + (100 * 5) + (litres - 250) * 10

print("Total Water Bill: Rs.", bill)

# 4.Create the Regular Expressions to fulfill the following instructions:
# i). to retrieve only single digits from a string.
# ii). to find the words starting with a number.

import re
text = "Here are some digits 1 3 5 and words like 1st, 2day, apple, 3rd."

# i) Retrieve only single digits
single_digits = re.findall(r'\b\d\b', text)
print("Single digits:", single_digits)

# ii) Find words starting with a number
start_with_number = re.findall(r'\b\d\w*', text)
print("Words starting with a number:", start_with_number)

# 5. Create a file write ‘Atmiya University’ into it. Modify the content of the file and
# write ‘Atmiya University, Rajkot’. Display the content of the file.

filename = "university.txt"

# Write initial content
with open(filename, "w") as file:
    file.write("Atmiya University")

# Modify content
with open(filename, "w") as file:
    file.write("Atmiya University, Rajkot")

# Display content
with open(filename, "r") as file:
    content = file.read()
    print("File Content:", content)

# 6. Accept the name of the file from the user. Check whether file exists or not. If the
# file exists display the content on the screen otherwise display the message that the
# file does not exist

import os
file_name = input("Enter the file name: ")

if os.path.exists(file_name):
    with open(file_name, "r") as file:
        print("File Content:\n", file.read())
else:
    print("File does not exist.")


# 7.Create a Bar chart that demonstrates number of admissions in MCA program in last
# of five years. Data input is to be taken from the of csv file 

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("admissions.csv")

plt.bar(data["Year"], data["Admissions"], color='teal')
plt.title("MCA Admissions in Last 5 Years")
plt.xlabel("Year")
plt.ylabel("Number of Admissions")
plt.grid(True, axis='y')
plt.show()

# Set E 

# 1. Draw the Scatter plot by assuming the appropriate data. 

import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [5, 7, 6, 8, 10]

plt.scatter(x, y, color='red')
plt.title("Sample Scatter Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True)
plt.show()

# 2. Create a regular expression that fulfills the following requirements:
# i). Retrieve the word starting with 'bs' and 'bm'
# ii). Retrieve the height of students. (i/p: abc 75)

import re
text = "bsc bms bca btech bme abc 75 xyz 82"

# i) Retrieve words starting with 'bs' or 'bm'
match_words = re.findall(r'\bbs\w*|\bbm\w*', text)
print("Matching words (bs/bm):", match_words)

# ii) Retrieve height (e.g. format: abc 75)
heights = re.findall(r'\b\w+\s\d+\b', text)
print("Height entries:", heights)

# 3. Create the Anonymous function that calculates square of the number.

square = lambda x: x ** 2
print("Square of 5:", square(5))  # Output: 25

# 4--Take the file and write data into it. Count and display number of lines, words and
# characters

file_name = "data.txt"

# Writing data
with open(file_name, "w") as file:
    file.write("Atmiya University\nLocated in Rajkot\nAI and Data Science")

# Reading and counting
with open(file_name, "r") as file:
    content = file.read()
    lines = content.splitlines()
    words = content.split()
    characters = len(content)

print("Lines:", len(lines))
print("Words:", len(words))
print("Characters:", characters)

# 5.Take the age of the policy holder and display appropriate discount based on the
# following conditions: Age<=20 than 20% discount, Age >=21 and <=30 18%
# discount, Age >=31 and <=40 15% and Age>=41 No discount. If the amount of
# yearly premium is Rs. 25000/- then how much amount of discount the customer will
# receive?

age = int(input("Enter the age of the policy holder: "))
premium = 25000

if age <= 20:
    discount = 0.20
elif age <= 30:
    discount = 0.18
elif age <= 40:
    discount = 0.15
else:
    discount = 0.00

discount_amount = premium * discount
print(f"Discount Received: Rs. {discount_amount}")
print(f"Final Amount to Pay: Rs. {premium - discount_amount}")

# 6. Create an array with appropriate numeric values. Convert the array to 2x3
# dimensions. Then convert it to the normal 1-dimension array

import numpy as np

array = np.array([10, 20, 30, 40, 50, 60])
reshaped_array = array.reshape(2, 3)
flattened_array = reshaped_array.flatten()

print("Original Array:", array)
print("Reshaped to 2x3:\n", reshaped_array)
print("Flattened Back to 1D:", flattened_array)

# 7. Create an array fill some values and perform the following tasks on it: insert value
# at the desired position, append the value, deleting the specific value, finding position
# of the specific element, convert array to list

import array

arr = array.array('i', [10, 20, 30, 40])

# Insert value at position 2
arr.insert(2, 25)

# Append value
arr.append(50)

# Remove specific value
arr.remove(20)

# Find position of specific element
pos = arr.index(30)

# Convert to list
arr_list = arr.tolist()

print("Modified Array:", arr)
print("Position of 30:", pos)
print("Converted to List:", arr_list)

# 8.Create a CSV file having 7 years and raise in the count of the population each year.
# Using this data, create a Bar chart. Everything must be properly labeled.

import pandas as pd
import matplotlib.pyplot as plt

# CSV creation
data = {
    "Year": [2017, 2018, 2019, 2020, 2021, 2022, 2023],
    "Population": [1000, 1200, 1400, 1650, 1800, 2100, 2300]
}
df = pd.DataFrame(data)
df.to_csv("population.csv", index=False)

# Read and plot
df = pd.read_csv("population.csv")

plt.bar(df["Year"], df["Population"], color='purple')
plt.title("Population Growth Over 7 Years")
plt.xlabel("Year")
plt.ylabel("Population")
plt.grid(axis='y')
plt.show()


# Set F 

# 1. Create an Area Plot by assuming the relevant data. 
import matplotlib.pyplot as plt

# Sample data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [200, 300, 250, 400, 350]

plt.fill_between(months, sales, color="skyblue", alpha=0.4)
plt.plot(months, sales, color="blue")
plt.title("Monthly Sales - Area Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# 2. Create the Regular Expressions to fulfill the following instructions:
# i). to find all the words starting with ‘a’.
# ii). to retrieve the words having 3 or more than 3 and less than 5 characters.
# iii). to retrieve only single digit number from the string

import re

text = "apple art act bat cat at 1 23 456 a123"

# i) Words starting with ‘a’
words_starting_a = re.findall(r'\ba\w*', text)

# ii) Words with 3 to 4 characters
words_3_to_4 = re.findall(r'\b\w{3,4}\b', text)

# iii) Single digit numbers
single_digits = re.findall(r'\b\d\b', text)

print("Words starting with 'a':", words_starting_a)
print("Words with 3 to 4 chars:", words_3_to_4)
print("Single digit numbers:", single_digits)

# 3. Take two image files, zip it and unzip it to a different location.

import zipfile
import shutil
import os

# Assume you have 'img1.jpg' and 'img2.jpg' in the current directory
with zipfile.ZipFile("images.zip", "w") as zipf:
    zipf.write("img1.jpg")
    zipf.write("img2.jpg")

# Unzip to a folder
unzip_location = "unzipped_images"
os.makedirs(unzip_location, exist_ok=True)
with zipfile.ZipFile("images.zip", "r") as zipf:
    zipf.extractall(unzip_location)


print("Images zipped and extracted successfully.")

# 4. Take the purchase amount from the user and calculate the following:
# If the amount is <=1000 the shipping charge will be 100, amount>1000 <=2000
# shipping will be 80, amount >2000<=3000 shipping will be 50, amount >3000
# shipping will be free and 10% bonus coins. Calculate the total amount to pay and
# bonus coins credited

amount = float(input("Enter purchase amount: "))
shipping = 0
bonus_coins = 0

if amount <= 1000:
    shipping = 100
elif amount <= 2000:
    shipping = 80
elif amount <= 3000:
    shipping = 50
else:
    shipping = 0
    bonus_coins = amount * 0.10

total = amount + shipping
print(f"Shipping Charges: Rs. {shipping}")
print(f"Total Amount to Pay: Rs. {total}")
print(f"Bonus Coins Credited: {bonus_coins}")

# 5. Create and array fill some numeric values into it. Add 2 to all the values, subtract 2
# from every value, find the maximum value, find sum and find average of all the
# values

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

added = arr + 2
subtracted = arr - 2
maximum = arr.max()
total = arr.sum()
average = arr.mean()

print("Original Array:", arr)
print("Add 2:", added)
print("Subtract 2:", subtracted)
print("Max:", maximum)
print("Sum:", total)
print("Average:", average)

# 6. Take sales of five months in the array, display total sales of five months and average
# sales.

sales = [12000, 13500, 11000, 14500, 13000]

total_sales = sum(sales)
average_sales = total_sales / len(sales)

print("Total Sales:", total_sales)
print("Average Sales:", average_sales)

# 7. Create an excel file, add 5 products and its sales in the last month. Create a Bar chart
# using the above data. Everything must be properly labeled.

import pandas as pd
import matplotlib.pyplot as plt

# Creating Excel file
data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"],
    "Sales": [150, 300, 200, 180, 90]
}
df = pd.DataFrame(data)
df.to_excel("product_sales.xlsx", index=False)

# Reading and plotting
df = pd.read_excel("product_sales.xlsx")
plt.bar(df["Product"], df["Sales"], color='orange')
plt.title("Product Sales - Last Month")
plt.xlabel("Product")
plt.ylabel("Units Sold")
plt.grid(True, axis='y')
plt.show()
