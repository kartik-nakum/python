
# # 1
basic=int(input('enter salary :'))
ta=basic*4/100
da=basic*30/100
hra=basic*15/100
tax=basic*3/100
pf=basic*12/100
find=basic+ta+da+hr
print(find)

# 2

import sys
a=int((sys.argv[1]))
b=int((sys.argv[2]))
c=int((sys.argv[3]))
d=int((sys.argv[4]))
e=int((sys.argv[5]))
total=a+b+c+d+e
print('total :',total)

per=total/5
print('Percentage:',per)

#3

a=int(input('bill amount :'))
if a<=90:
	print('rs. 0/itr',a)
elif a<=150:
	print('rs.2/ltr',a*2)
elif a<=250:
     print('rs.5/ltr',a*5)	
elif a>250:
	 print('rs.10/lrt',a*10)
else:
	print('not bill')

#4

stu=int(input("enter student marks :"))
if stu>90 :
	print('A1 grade')
elif stu>80 and stu<=90:
	print('A grade')
elif stu>70 and stu<=80:
	print('B1 grade')
elif stu<60 and stu<=70:
	print('B grade')
elif stu>50 and stu<=60:
	print('can do better!')
elif stu>50 :
	print('need to work hard')	
else:
	print('number')					


#5
tax=0
inc=int(input("enter student marks :"))
if inc<=800000 :
	print(tax,'no tax')
elif inc>800000 and inc<=1000000:
	tax1=inc*15/100
	print(tax1,'15% tax')
elif inc>1000000 and inc<=2000000:
	tax2=inc*20/100
	print(tax2,'20% tax')
elif inc>2000000 :
	tax3=inc*30/100
	print(tax3,'30% tax')
else:
	print('number')

# 6

a=int(input('enetr value a'))
b=int(input('enter value b'))

if a>b:
	print('a is bigger')
else :
	print('a is small')	
if b>a:
	print('b is bigger')
else :
	print('b is small')	

# #7

a=[0]*4
for i in range(4):
   a[i]=int(input('enter student marks :'))
hi=max(a)
print(hi)
    
   #8

amount=int(input('enter amount :'))
if amount<=1500:
     print('please purchase',(1500-amount),'to avail shipping charges is Rs.80')
     print('please pay :',amount+100) 
elif amount>1500 and amount<=3000:
    print('please purchase',(3000-amount),'to avail shipping charges is Rs.80') 
    print('please pay:',amount+70) 
elif amount>3000 :
    did=amount*7/100
    print('your saved',did)
    print('please pay :',amount-did)