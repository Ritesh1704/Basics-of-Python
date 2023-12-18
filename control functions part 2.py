#!/usr/bin/env python
# coding: utf-8

# # Flow Control Structures

# ## `if statement`

# #### Syntax of `if` statement`
if <expr>:
    <statement(s)>
    
--> <expr> is an expression evaluated.
--> <statement> is a valid Python statement, which must be indented

If <expr> is true, then <statement> is executed. 
If <expr> is false, then <statement> is skipped over and not executed.
# In[6]:


x = 22 #initialize x

if x<20: #expression / criteria
    print(x,'is less than 20') #if statement which will be executed given criteria is satisfied #Indentation: 1 tab = 4 whitespaces
    
print('Done')


# In[9]:


x=100
if x<20: #expression / criteria
    print(x,'is less than 20')
    print('Welcome to Python Course')
    print('Today we are learning flow control structures')
    print(100*100)
    
print('Done')


# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# #### Flow diagram

# ![image.png](attachment:image.png)

# ###  `if else` statement

# - Sometimes we want to do one thing if a logical expression is `True` and something else if the expression is `False`
# - It is like a fork in the road (refer the above image) - we must choose one or the other path but not the both

# ![image.png](attachment:image.png)

# ![image-2.png](attachment:image-2.png)
# `credit to the creator`

# ### User Input 

# In[11]:


user_input = input('Enter integer:') #user input
print(type(user_input))


# #### Typecasting => converts one data type to other

# In[15]:


user_input = int(input('Enter integer:')) #user input
print(type(user_input))


# In[24]:


user_input = int(input('Enter integer:')) #user input

if user_input >100:
    print('more than 100') #if statement
else:
    print('less than 100') #else statement

print('Done')


# In[21]:


x='100'
y = int(x)
print(type(x))
print(type(y))


# #### `Nested if statement` with user input

# In[35]:


user_input = int(input('enter integer :'))
print(type(user_input))


# ![image.png](attachment:image.png)

# In[39]:


user_input = int(input('Enter an integer :'))

if user_input >100:
    print('more than 100')
    
    if user_input <1000:
        print('More than 100 but less than 1000')
        
        
print('Done')


# #### Case 1: Both if statements are true

# ![image.png](attachment:image.png)

# #### Case 2: Inner if statement is false but outer if is true

# ![image.png](attachment:image.png)

# #### Case 3: Both if statements are false

# ![image.png](attachment:image.png)

# - Python evaluates nested if statement when the condition of the preceding `if statement` is True
# - When the condition is False for the preceding `if statement`, nested if statment doesnt run

# ###  `nested if else` statement

# In[41]:


##nested if

numa = 15
numb = 20

if(numa>10):
    if(numb>=11):
        print("b greater than 11")
    else:
        print("b less than 11")
else:
    print("a less than 10")


# In[42]:


user_input = int(input('Enter an integer:')) #user input


if user_input > 100:
    print('More than 100')
    
    if user_input <1000:
        print('More than 100 but less than 1000')
        
    else:
        print('More than or equal to 1000')

else:
    print('Less than or equal to 100')
    print('Outer if condition is false hence it did not even enter the nested if else condition')
        
        
print('Done')


# ![image.png](attachment:image.png)

# ### - H/W: Write a program to display the greatest among three numbers using `nested if` statement
# `Numbers should be taken as user input`
# 
# `With error/exception handling`
# 
# `Do not use anything fancy`

# ###  ` if... elif... else` statement

# ![image.png](attachment:image.png)
# `credit to the creator`

# - is used to make choices/decisions between more than two alternatives
if condition1:
    # code block 1

elif condition2:
    # code block 2

else: 
    # code block 3
# In[46]:


num = float(input("Enter the number:"))


if num >0:
    print('Positive number')
    
elif num==0:
    print('Zero')
    
else:
    print('Negative number')
    

print('Done')


# #### `Shorthand` if else statement

# In[54]:


a = 10
b = 20

print('Num a', a, 'is greater than b', b) if a > b else print('equal:', a) if a == b else print('Num a', a, 'smaller than b', b)


# ### BESCOM ELECTRICITY BILL CALCULATOR ASSESSMENT
# `© APC`

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# ### Due Date: 9th Jul - Soft deadline & 16th Jul - Hard deadline
# `Minimum 10 Submissions using Jupyter notebook`

# ## Loops in Python

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# ![image-2.png](attachment:image-2.png)

# ![image.png](attachment:image.png)

# In[5]:


num = [10, 20, 30, 40,50]
print(num)
print(type(num))


# In[12]:


for i in num:
    print('The number is:', i*2)


# ### Element-wise multiplication of two lists:

# In[13]:


list1 = [1,2,3]
list2 = [4,6,8]


# `expected output: [4,12,24]`

# In[17]:


print(list1)
print(list2)


# In[16]:


list1*list2


# - Python does not have built-in vectorized operation

# #### Using for loop

# In[39]:


list1 = [1,2,3]
list2 = [4,6,8]The range() function returns a sequence of numbers starting from 0 (by default) if the initial limit is not specified and it increments by 1 (by default) until a final limit is reached.

The **`range()`** function is used with a loop to specify the range (how many times) the code block will be executed. Let us see with an example.

We can generate a sequence of numbers using **`range()`** function. **`range(5)`** will generate numbers from 0 to 4 (5 numbers). 


# Iterate over the indices of both the lists:
result=[] #empty list

for i in range(len(list1)):
    #Multiply and append the result to the empty list:
    print("Iteration:", i)
    result.append(list1[i]*list2[i])
    
print('Multiplication of two lists is:', result)


# ![image.png](attachment:image.png)

# ## Why use `for` loop?
# 
# Let’s see the use **`for`** loop in Python.
# 
# * **Definite Iteration:** When we know how many times we wanted to run a loop, then we use count-controlled loops such as **`for`** loops. It is also known as definite iteration. For example, Calculate the percentage of 50 students. here we know we need to iterate a loop 50 times (1 iteration for each student).
# * **Reduces the code’s complexity:** Loop repeats a specific block of code a fixed number of times. It reduces the repetition of lines of code, thus reducing the complexity of the code. Using **`for`** loops and while loops we can automate and repeat tasks in an efficient manner.
# * **Loop through sequences:** used for iterating over lists, strings, tuples, dictionaries, etc., and perform various operations on it, based on the conditions specified by the user.

# ## `for` loop with `range()` function

# The range() function returns a sequence of numbers starting from 0 (by default) if the initial limit is not specified and it increments by 1 (by default) until a final limit is reached.
# 
# The **`range()`** function is used with a loop to specify the range (how many times) the code block will be executed. Let us see with an example.
# 
# We can generate a sequence of numbers using **`range()`** function. **`range(5)`** will generate numbers from 0 to 4 (5 numbers). 

# In[40]:


range(5)


# In[41]:


list(range(5))


# In[43]:


list(range(10))


# In[44]:


list(range(10,101,5))


# ![image.png](attachment:image.png)

# ## Sum of consecutive natural numbers

# - Write a for loop code to do the sum of 'n' natural numbers
# - 'n'should be an user input
# 
# `Guideline`
# 
# 
# **Need to use** `for loop` and `range()`
# 
# **DO NOT USE THE STD. FORMULA = n(n+1)/2**

# In[52]:


n = int(input('Enter the natural number till which sum is required:'))

total = 0

for i in range(1, n+1):
    total = total + i 
    
print("Sum of the first", n, "natural numbers is:", total)


# In[53]:


n=10
print(list(range(1,n)))
print(list(range(1,n+1)))
print(list(range(1,n+2)))


# ## H/W Q Calculate the sum of square of `n` natural numbers
# 
# **Need to use** `for loop` and `range()`
# 
# **DO NOT USE THE STD. FORMULA**
# 

# ![image.png](attachment:image.png)

# ## Conditional Loops: `for` loop with `if-elif-else`

# A **`for`** loop can have an optional [if-else] block. The **`if-else`** checks the condition and if the condition is **`True`** it executes the block of code present inside the **`if`** block and if the condition is **`False`**, it will execute the block of code present inside the **`else`** block.

# In[ ]:


ages = [15,20,25,30,35,40,50,60,62,80,90,99]

#ages_category

# age <=10, kid
# age<=18, teenager
# age<=30, young
# age<=45, adult
# age<=60, middle-age
# age<=75, senior citizen
# age>75, super senior citizen


# `Age: 20 Category: young`
# 
# `Hint: Think about tuple being stored in a list`

# In[56]:


ages = [15,20,25,30,35,40,50,60,62,80,90,99] #Amit
 
ages_Category = []

for i in ages:
    if i <=10:
        ages_Category.append(['age:', i, 'category: Kid'])
    elif i <= 18:
        ages_Category.append(['age:', i, 'category: Teenager'])
    elif i <= 30:
        ages_Category.append(['age:', i, 'category: Young'])
    elif i <= 45:
        ages_Category.append(['age:', i, 'category: Adult'])
    elif i<=60:
        ages_Category.append(['age:', i, 'category: Middle Age'])
    elif i<=75:
        ages_Category.append(['age:', i, 'category: Senior Citizen'])
    else:
        ages_Category.append(['age:', i, 'category: Super Senior Citizen'])
        
print(ages_Category)


# In[57]:


ages = [15,20,25,30,35,40,50,60,62,80,90,99] #Arpan
 
final_list = []

for age in ages:
    if (age <= 10):
        final_list.append((age,"kid"))
    elif (age < 18):
        final_list.append((age,"teenager"))
    elif (age <= 30):
        final_list.append((age,"young"))
    elif (age<= 45):
        final_list.append((age,"adult"))
    elif (age <= 60):
        final_list.append((age,"middle-age"))
    elif (age <= 75):
        final_list.append((age,"senior citizen"))
    elif (age > 75):
        final_list.append((age,"super senior citizen"))
    else:
        print("No category")
        
print(final_list)


# In[59]:


ages = [15,20,25,30,35,40,50,60,62,80,90,99]  #Satyam
output = []
for i in range(len(ages)):
    print(ages[i])
    if(ages[i]<=10):
        output.append({'Age':ages[i], 'Category': 'kid'})
        print('Age:',ages[i], 'Category: kid')
    elif(ages[i] <= 18):
        output.append({'Age': ages[i], 'Category':'teenager'})
    elif(ages[i] <= 30):
        output.append({'Age': ages[i], 'Category': 'young'})
    elif(ages[i] <= 45):
        output.append({'Age': ages[i], 'Category': 'adult'})
    elif(ages[i] <= 60):
        output.append({'Age': ages[i], 'Category': 'Middle Age'})
    elif(ages[i] <= 75):
        output.append({'Age': ages[i], 'Category': 'senior citizen'})
    else:
        output.append({'Age': ages[i], 'Category': 'super senior citizen'})

print(output)


# ![image.png](attachment:image.png)

# In[ ]:


# age <=10, kid
# age<=18, teenager
# age<=30, young
# age<=45, adult
# age<=60, middle-age
# age<=75, senior citizen
# age>75, super senior citizen


# In[61]:


ages = [15,20,25,30,35,40,50,60,62,80,90,99]

ages_categories = []


for age in ages:
    if age <=10:
        category='kid'
    elif age <=18:
        category='teenager'
    elif age <=30:
        category='young'
    elif age <=45:
        category='adult'
    elif age <=60:
        category='middle-age'
    elif age <=75:
        category='senior citizen'
    else:
        category='super senior citizen'
    
    ages_categories.append((age,category))


# In[62]:


ages_categories


# In[63]:


for age, category in ages_categories:
    print("Age:", age, "Category:", category)


# #### How can we store in the form list of dictionary and then access it using for loop

# In[64]:


ages = [15,20,25,30,35,40,50,60,62,80,90,99]

ages_categories = []


for age in ages:
    if age <=10:
        category='kid'
    elif age <=18:
        category='teenager'
    elif age <=30:
        category='young'
    elif age <=45:
        category='adult'
    elif age <=60:
        category='middle-age'
    elif age <=75:
        category='senior citizen'
    else:
        category='super senior citizen'
    
    ages_categories.append({'age':age, 'category': category})


# In[65]:


ages_categories


# In[67]:


for element in ages_categories:
    print("Age:", item['age'], "Category:", item['category'])


# ![image.png](attachment:image.png)

# In[79]:


age=[15,20,25,30,35,40,50,60,62,80,90,99]
age1=range(0,11)
age2=range(11,20)
age3=range(21,31)
age4=range(31,46)
age5=range(46,61)
age6=range(61,76)
age7=range(76,100)

Prt_age={age1:'Kid', age2:'Teenage', age3:'Young', age4:'Adult', age5:'Middle age', age6:'Senior citizen', age7:'Super Senior citizen'}


# In[80]:


Prt_age


# In[81]:


for i in (len(age)):
    if i==age1[i]:
        print(i,"belongs to", Prt_age{i})
    print('Done')


# In[82]:


for i in range(len(age)):
    for age_range, category in Prt_age.items():
        if age[i] in age_range:
            print(age[i], category)


# In[87]:


age=[int(input("Enter the age:"))]
age1=range(0,11)
age2=range(11,20)
age3=range(21,31)
age4=range(31,46)
age5=range(46,61)
age6=range(61,76)
age7=range(76,100)

Prt_age={age1:'Kid', age2:'Teenage', age3:'Young', age4:'Adult', age5:'Middle age', age6:'Senior citizen', age7:'Super Senior citizen'}


for i in range(len(age)):
    for age_range, category in Prt_age.items():
        if age[i] in age_range:
            print(age[i], category)


# In[84]:


Prt_age.items()


# ### Nested `for` loop

# ![image.png](attachment:image.png)

# #### Multiplication table

# In[93]:


for i in range(1,11):
    for j in range(1,11):
        print(i*j, end= " ")#body of inner loop
    print('') #creating a new line

print('Done')


# ### Write a `nested for loop` to print the image shown below:
# ![image.png](attachment:image.png)

# In[97]:


star_num = int(input('Enter positive integer:'))

for i in range(1, star_num+1):
    for j in range(i):
        print("*", end=" ")
    print()
    


# In[98]:


first_names = ['Akash', 'Vikas', 'Anand']
last_names = ['Kumar', 'Ranjan']

### Print all the combinations of first name with the last name


# In[101]:


first_names = ['Akash', 'Vikas', 'Anand'] 
last_names = ['Kumar', 'Ranjan']

for i in first_names: #using i, pick one first name
    for j in last_names: #using j, creating all the combinations of first name & laast names
        print(i + " " + j)


# ## While Loop

# ![image.png](attachment:image.png)

# #### Python `while` loop is used to run a block of code until a  certain condition is met

# #### Program to display 100 natural numbers

# In[105]:


start=1
stop=100


while start <=stop:
    print(start, end= " ")
    start = start + 1
    
print("| Done")
    


# ## Break, Continue and Pass

# ### Break

# - it will stop execution of the `for` loop when break command is executed (breaks & come out of the loop)
# - break terminates the current loop given the condition satisfies if used with `conditional` statements

# In[111]:


num = [10,20,30, 40, 150, 60, 70 ,80]


# #### Print the all the numbers in the above list below 100

# In[112]:


for i in num:
    if i>=100:
        break
    print('Current number is:', i)
    
    
print('Out of the for loop')


# ![image.png](attachment:image.png)

# In[ ]:




