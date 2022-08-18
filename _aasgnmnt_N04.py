#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Answer no.1
#python program for finding factorial number
num = 7
#To take input from user
#num = int(input("Enter a number"))
factorial = 1
if num < 0 :
    print("Its a negative number")
    
elif num == 0:
    print("factorial of 0 is 1")
    
else:
    for i in range(1,num+1):
        factorial = factorial*i
    print("The factorial of",num,"is",factorial)


# In[10]:


#Answer no.2
#python program for multiplaction table : 
num = int(input("Display multiplication table of :"))
for i in range(1,11):
    print(num,'x',1,'=',num*i)


# In[12]:


#Answer no.3
#python program for fibonacci sequence
num = int(input("How many terms?"))
n1,n2 = 0,1
count = 0
if num <= 0:
    print("Please enter a positive integer")
    
elif num == 1:
    print("fibonacci sequence upto",num,":")
    print(n1)
    
else:
    print("fibonacci sequence")
    while count < num:
        print(n1)
        numth = n1 + n2
        # update values
        n1 = n2
        n2 = numth
        count +=1


# In[17]:


#Answer no.4
#python program for armstrong number
num = int(input("Enter a number:"))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum+= digit ** 3
    temp//= 10
    
if num == sum:
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")
    



# In[19]:


#Answer no.5
#Python program to check armstrong number in intervals
a = 100
b = 2000
for num in range(a,b+1):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0 :
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    if num == sum:
        print(num)
        


# In[20]:


#Answer no.6
num = 18
if num < 0:
    print("Enter positive number")
else:
    sum = 0
    while (num > 0):
        sum += num
        num -= 1
    print("the sum is",sum)
    


# In[ ]:




