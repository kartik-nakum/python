# Unit-5
#to read that.csv file in python
import pandas as pd 
df=pd.read_csv('product.csv')
print(df)

#knowing number of rows and numberof colums
print(df.shape)
# display first 5 records
print(df.head(6))
# display last 5 records
print(df.tail())
# display last 2 records
print(df.tail(2))
# display data in range
print(df[3:8])
# retrieving the data from the particular colums
print(df[['NAME','PRICE']])
# Finding maximum value records
print(df['PRICE'].max())
# Finding minimum value records
print(df['PRICE'].min())
# display product whose category is 'Electroincs'
print(df[df.CATEGORY=='Electroinic'])
# display product whose price it more than 250
print(df[df.PRICE>250])
# display only product name whice belongs to category 'Electroincs'
print(df[['NAME']][df.CATEGORY=='Electroinic'])

# import pandas as pd 
import xlrd
df=pd.read_excel('product1.xlsx')
print(df)

#reading the data from python dictionary
import pandas as pd 
student={'enr':[101,102,103,104,105],'name':['abc','cde','efg','ghi','ijk'],'city':['rajkot','matura','vrundavan','ayodhya','prayagraj']}
df=pd.DataFrame(student)
print(df)

# reading thr data from python tuple
import pandas as pd 
student=[(101,'abc','rajkot'),(102,'cde','matura'),(103,'efg','vrundavan'),(104,'ghi','ayodhya'),(105,'ijk','prayagraj')]
df=pd.DataFrame(student,columns=['Enrol','Name','City'])
print(df)


# Visualising the data
# Bar Chart
import pandas as pd 
import matplotlib.pyplot as plt 
df=pd.read_excel('book1.xlsx')
print(df)
x=df['year']
y=df['sales_of_unit']
plt.bar(x,y,label='Year wise sales of books',color='Red')
# plt.bar(x,y)
plt.xlabel('Year')
plt.ylabel('Units')
plt.title('XYZ Book Store')
plt.legend()
plt.show()

# Pie Chart
import matplotlib.pyplot as plt 
sales_Per=[15,20,10,25,20]
comp_name=['Natraj','Apsara','Doms','ABC','Camlin']
col=['red','green','blue','yellow','pink']
plt.pie(sales_Per,labels=comp_name,colors=col)
plt.title('Sales of Pencil in India')
plt.legend()
plt.show()

# Line Chart
import matplotlib.pyplot as plt
Years=['2020','2021','2022','2023','2024']
inc_decr_sales=[75,25,45,50,79]
# Years=['2020','2021','2022','2023','2024']
inc_decr_sales1=[65,45,25,65,90]
plt.plot(Years,inc_decr_sales,color='red')
plt.plot(Years,inc_decr_sales1,color='blue')
plt.title('Increase/Ddecrease in sales')
plt.show()

# # Scatter Chart
import matplotlib.pyplot as plt
inc_decr_sales=[75,25,45,50,79]
inc_decr_sales1=[65,45,25,65,90]
plt.plot(inc_decr_sales,inc_decr_sales1)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Scatter diagram')
plt.show()

# Area plot
import matplotlib.pyplot as plt
import numpy as np 
inc_decr_sales=[2,4,6,5,4]
x=range(1,6)
inc_decr_sales1=[1,4,6,2,4]
plt.fill_between(x,inc_decr_sales1)
plt.title('Area Ploat')
plt.show()