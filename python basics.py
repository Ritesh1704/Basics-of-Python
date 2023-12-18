#!/usr/bin/env python
# coding: utf-8

# # Welcome to Python Basics - `Day#02`
# `Instructor - APC`

# - Green border around the cell means `Edit Mode`
# - Blue border around the cell means `Command Mode`
# **Press Esc to go from edit mode to command mode**

# - In the command mode, 
#     1. Press 'B' to add cell below the current cell
#     2. Press 'A' to add cell above the current cell
#     3. Press 'D', 'D' to delete selected cells

# ![image.png](attachment:image.png)

# ### Few Command mode shortcuts

# ![image.png](attachment:image.png)

# ### Headings
# for the titles
## for the main headings
### for the subheadings
#### for the smaller subheadings
##### for the italic subheadings
# # Python Class

# ## Python Class

# ### Python Class

# #### Python Class

# ##### Python Class

# ### How to insert an image /screenshot in Jupyter notebook

# #### Step1: Be ready with image screenshot `( Windows + Shift + S)`

# #### Step2: Paste the link for the screenshot in the cell making it in markdown type

# ![image.png](attachment:image.png)

# ### Emphasis
•	__string__ or **string** for bold text
•	_string_ or *string*  for italic text
# Welcome to Python Basic course. Your instructor is **APC**

# Welcome to Python Basic course. Your instructor is __APC__

# Welcome to Python Basic course. Your instructor is _APC_

# Welcome to Python Basic course. Your instructor is *APC*

# ### Monospace

# A **back** single quoation mark `(above the 'tab'button, on the same button which is having ~) to get monospace fonts

# `Happy Learning`

# ### Bullets & Numbering
A single dash, i.e., - followed by one/two spaces to make bullet points
A number and a dot followed by a single space, i.e., to make numbered lists
# - Hello Students!

# 1. Amit
# 2. Pran
# 3. Allan

# https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Working%20With%20Markdown%20Cells.html

# https://www.markdownguide.org/cheat-sheet/

# ### Line Breaks

# Lorem Ipsum is simply dummy text of the printing and typesetting industry. <br> Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.<br> It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, <br> and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

# ## PythonTutor can be used to visualize your code

# https://pythontutor.com/visualize.html#mode=edit

# ## Python Variables

# In[15]:


print('Hello World')

### Lines of code in C to print Hello World

#include <stdio.h>
int main() {
   // printf() displays the string inside quotation
   printf("Hello, World!");
   return 0;
}
# In[16]:


2+3


# In[18]:


x = 10 
print(x)
print(type(x))


# In[19]:


my_string = "Welcome to Basic Python course"
print(my_string)
print(type(my_string))


# `tab` : `to auto complete the part of the code`
# 
# `shift + tab`: `to see the documentation for the selected function/keyword`

# ### Variable naming conventions

# In[21]:


7dhoni = 'CSK wins IPL 2023'


# In[22]:


dhoni7 = 'CSK wins IPL 2023'


# In[23]:


dhoni7


# In[24]:


_7dhoni = "MSD"


# In[25]:


_7dhoni


# In[26]:


__12_apc_13 = 'My name is Akash'


# In[31]:


print(__12_apc_13)


# In[28]:


pass = "I have passed the Python test"


# In[29]:


dhoni@007 = "MSD"


# In[30]:


def =100


# #### Keywords in Python

# - special reserve words for coding 
# - have special meaning and purposes
# - Can't be used for variable names

# In[32]:


help('keywords')


# In[33]:


my_string = "welcome to Python course"
print(my_string)
print(type(my_string))


# In[34]:


false = "APC"


# In[37]:


false


# ### How to delete a variable

# In[38]:


del my_string #deleted the variable 'my_string'


# In[39]:


print(my_string)


# #### how can we see all created variables #lakshmi

# In[41]:


dir()


# In[42]:





# #### x=null vs del x what is the difference

# In[50]:


x


# In[51]:


x='hello world'
print(x)
print(type(x))


# In[52]:


y='10'
print(x)
print(type(x))


# In[57]:


x =100
y ='100'
print('x:',x)
print('y:',y)
print('data type of x is:', type(x))
print('data type of y is:',type(y))


# ### Single, Double, Triple Quotes

# #### Single line statement

# In[58]:


my_line = 'Today is the second session on Basic Python' #single quotes
print(my_line)


# In[60]:


my_line_dq = "Today is the second session on Basic Python" #double quotes
print(my_line_dq)


# In[61]:


my_line_tq = '''Today is the second session on Basic Python'''#triple single quotes
print(my_line_tq)


# In[62]:


my_line_tq2 = """Today is the second session on Basic Python""" #triple double quotes
print(my_line_tq2)


# #### Single quote doesn't work

# In[63]:


my_info = 'Today's class is going great' #using apostrophe s


# In[64]:


my_info = "Today's class is going great" #using apostrophe s + double quotes
print(my_info)


# In[76]:


my_info1 = '''Today's class is going great''' #using apostrophe s + triple single quotes
print(my_info1)


# #### Escaping Behaviors

# In[67]:


my_info = 'Today\'s cla\'ss is go\'ing great' #using apostrophe s + backslash
print(my_info)


# In[69]:


my_info_2 ="Today\'s class is going great, \"Thank You\""
print(my_info_2)


# In[75]:


my_text = "Today\'s class is going great, \"Thank You\" "
print(my_text)


# #### Multiple Line Statement

# In[80]:


my_note = "This is our Python class.
It's going great.
We are coding with the trainer."

print(my_note)


# In[81]:


my_note = '''This is our Python class.
It's going great.
We are coding with the trainer.'''

print(my_note)


# In[79]:


my_line="i am happy \n thank you"
print(my_line)


# # Welcome to Python Basics - `Day#03`
# `Instructor - APC`

# ## Operators

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# ### Arithmetic Operators

# - Used to perform mathematical operations like addition, subtraction, multiplication, division and many more

# ![image.png](attachment:image.png)

# In[1]:


a=11
b=2

#addition 
print('Sum:', a+b)

#subtraction
print('Difference:', a-b)

#multiplication
print('Product:', a*b)

#division
print('Division:', a/b)


# ### Floor division 

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# In[2]:


a=11
b=2

#addition 
print('Sum:', a+b)

#subtraction
print('Difference:', a-b)

#multiplication
print('Product:', a*b)

#division
print('Division:', a/b)

#Exponentiation (Power)
print('Power of a to b is:', a**b)

#Floor Division
print('Floor division:', a//b)

#Modulus (remainder)
print('Modulus:', a%b)


# ### Order of precedence

# ![image.png](attachment:image.png)

# ### Q. Solve the expressions as per precedence rule

# In[9]:


a=11
b=2
c=5
d=3


# #### a.

# In[10]:


a+b*c//d


# #### b.

# In[11]:


(a+b)*c//d


# ### Comparison Operators

# ![image.png](attachment:image.png)

# In[17]:


a=11
b=5

#smaller
print('Is it smaller:', a<b)

#smaller or equal to 
print('Is it smaller or equal to:', a<=b)

#greater
print('Is it greater:', a>b)

#greater or equal to 
print('Is it greater or equal to:', a>=b)

#equal
print('Is it equal:', a==b)

#Not euqal 
print('Is it not equal:', a!=b)


# - Comparison operators are used in decision making while creating flags in dataframe or in loop

# ### Comparison Operators

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# In[ ]:


a=10
b=100


# In[19]:


a>8 #Comparison operator


# In[20]:


b<10 #Comparison operator


# #### AND

# In[21]:


a>8 and b<10  #combination of comparison and logical operators


# #### OR

# In[23]:


a>8 or b<10  #combination of comparison and logical operators


# #### NOT

# In[24]:


not(a>8 or b<10) #combination of comparison and logical operators


# In[25]:


a>8 and b>8


# ### Assignment Operators

# - Assignment operators are used to assign values to variables

# #### Assign value `10` to variable `x`

# In[27]:


x=10


# ![image.png](attachment:image.png)

# In[36]:


a=10 #assignment operator
print(a)


# In[37]:


a+=20 #addition assignment operator
print(a)


# In[39]:


b=100
print(b)
b-=50
print(b)


# In[41]:


b=-50
print(b)
b-=50
print(b)


# In[40]:


c=100
print(c)
c*=100
print(c)


# ### H/W Try all the different assignment operators in the similar fashion

# ![image.png](attachment:image.png)

# ### Bitwise Operators

# - Bitwise operators are used to compare binary values

# ![image.png](attachment:image.png)

# ### Reading Assignment : Bitwise  Operators

# ### Membership Operators

# In[45]:


num =7 
num_list = [99,1,0.04, 'APC', 7, 1000, 99, 'My name is Akash']


# In[46]:


num==num_list[0] #0 is index postion 


# In[47]:


num==num_list[1]


# In[57]:


num==num_list[4]


# In[52]:


num_list[4]


# In[49]:


num==num_list[6]


# In[51]:


num in num_list


# - Using membership operator, we can check a Python list, string, tuple for membership
# - To check if any sequence is present in any object, we use `in` membership operator
# - To check if any sequence is `not` present in any object, we use `not in` membership operator

# In[55]:


text = "BBC"
text in num_list


# In[56]:


text = "APC"
text in num_list


# ### Identity Operators

# - In principle, Python is `object-oriented programming` language
# - Every object will have some identity in memory
# - There are two identity operators: `is` and `is not`
# - Binary operations returning boolean output

# ![image.png](attachment:image.png)

# In[60]:


x=10
print('ID of x is:',id(x))

y=10
print('ID of y is:', id(y))

z= '10'
print('ID of z is:', id(z))


# In[61]:


x is y #Is identity of x and y same?


# In[62]:


x is z #Is identity of x and z same?


# In[63]:


x is not z #Is identity of x and z not same?


# In[64]:


x=100
id(x)


# In[65]:


hex(id(x)) 


# In[69]:


x=10
print('ID of x is:',id(x))

y=10
print('ID of y is:', id(y))

z= '10'
print('ID of z is:', id(z))

x= '10'
print('ID of x is:', id(x))


# ## Data Types

# ### Numeric Data Types

# - Python has three built-in numeric data types: `integers`, `floating-point numbers`, and `complex numbers`

# #### Integer

# - An integer is a whole number with no decimal places --> Positive integers
# - Integers can be negative as well positive numbers
# - 0 is also an integer

# In[72]:


x = 0
type(x)


# In[73]:


my_int = 100
print(my_int)
print(type(my_int))


# In[76]:


import sys 
sys.getsizeof(my_int) #size in bytes


# ![image.png](attachment:image.png)

# - By default, `int` has 32 bits or 4 bytes of memory 

# In[81]:


my_int = 1000000000000000000000000000000000000000000000000000000000000000
sys.getsizeof(my_int)


# #### Float

# - A float is a number with `decimal places`

# In[82]:


my_float=2.0
print(my_float)
print(type(my_float))


# In[83]:


my_float=22.7867657775755
print(my_float)
print(type(my_float))


# In[84]:


sys.getsizeof(my_float)


# #### Typecasting

# - It is a method to change the variables/values declared in a certain data type into a different data type to match the operations requirements

# #### Implicit Typecasting

# - Implicit type casting occurs `automatically`  when the programming language converts one data type to another without any explicit instructions from the programmer

# In[107]:


num_int = 5
print(type(num_int))

num_float = 3.14
print(type(num_float))

result = num_int + num_float
print(type(result))


# #### Explicit Typecasting

# - It is a manual conversion by programmer of a variable from a one data type to another
# - In python, the `int()`, `float()`, `str()` and other similar functions are used for explicit typecasting

# In[110]:


num_int = 5
print(type(num_int))

num_float_conv = float(num_int)
print(type(num_float_conv))


# In[85]:


my_num= "1.25"
print(my_num)
print(type(my_num))


# In[86]:


my_float_conv = float(my_num) #forcing my_num from 'str' to 'float'
print(my_float_conv)
print(type(my_float_conv))


# `float()`: Convert a string or number to a floating point number, if possible.

# In[87]:


my_num= "APC"
print(my_num)
print(type(my_num))


# In[88]:


my_float_conv = float(my_num) #forcing my_num from 'str' to 'float'
print(my_float_conv)
print(type(my_float_conv))


# In[95]:


my_num = 123.45
print(my_num)
print(type(my_num))


# In[96]:


num_str = str(my_num)
print(num_str)
print(type(num_str))


# In[97]:


one_million = 1000000 #1million is equal to 10 lakhs
print(one_million)
print(type(one_million))


# In[98]:


one_million = 1000000.0 #1million is equal to 10 lakhs
print(one_million)
print(type(one_million))


# In[99]:


one_million = 1e6 #scientific notation
print(one_million)
print(type(one_million))


# #### Large float numbers are represented in `E` notation

# In[104]:


a= 200000000000000000000000.0 
print(a)


# In[105]:


a*1e-20


# In[106]:


1e-3


# `+` sign means power,`e` means 10, `23` raised to the power 23

# # `Day#04`|

# #### Complex

# - To create a complex number in Python, simply write the real part then +/- the imaginary part with the letter `j`

# In[1]:


my_complex= 2+3j
print(my_complex)
print(type(my_complex))


# ## Sequence Data Types

# ![image.png](attachment:image.png)

# ### List Data Type

# - List is an **ordered** collection of similar or different(hetereogenous) types of items/elements, separated by comma and enclosed with brackets [ ]
# - Lists are **mutable** which means that items/elements in the list can be modified (Ref: X-Men)

# ![image.png](attachment:image.png)

# #### Create a Python list

# ![image.png](attachment:image.png)

# In[3]:


my_list=[] #an empty list
print(my_list)


# #### Initialize the empty list

# In[4]:


my_list = [100,"APC", 7.0,3+5j,3.14, "BBC",-10, 1.33333]


# In[5]:


print(my_list)


# In[6]:


print(type(my_list))


# In[7]:


my_list[0] #value at 0th location => first element in the list


# In[8]:


my_list[1]


# In[9]:


my_list[6]


# In[10]:


print(type(my_list[0]))


# In[11]:


print(type(my_list[1]))


# In[12]:


print(type(my_list[2]))


# In[13]:


### Classes and methods in the 'list' data type
dir(list)


# ### Accessing Python list elements

# In[15]:


print(my_list)


# ### Slicing a list

# ![image.png](attachment:image.png)

# ##### Print all the items in list (do not use the above appraoch)

# In[25]:


my_list[::] #prints all the list


# ##### Print all the items in list starting from "APC"

# In[26]:


my_list[1::] #by default till the end with stpe size 1


# In[27]:


my_list[: :2] #prints the alternate elements starting from beginning


# ##### Show everything except the last element

# In[41]:


my_list[7]


# In[42]:


my_list[-1]


# In[43]:


my_list[: 7:]


# In[44]:


len(my_list) # len of list => number of elements in the list


# In[45]:


my_list[: len(my_list)-1 : ] #dynamic


# In[46]:


my_list[: -1 :] #already dynamic


# ##### Show everything except the three last elements

# In[47]:


my_list[: -3 :]


# ##### Show everything except the starting two elements

# In[48]:


my_list[2: :]


# ##### Show the list in the reverse order

# In[39]:


my_list


# In[51]:


my_list[: : -1]


# ##### Show the list in the reverse order printing alternate items

# In[52]:


my_list[: : -2]


# ### Lists: Mutable & Dynamic
# `pro tip`

# - Elements can be modified
# - Elements can be deleted
# - Order of the elements can be changed

# In[55]:


my_list


# In[58]:


#Change BBC to RCB
my_list[5] = 'RCB' #changing the value from 'BBC' to 'RCB'
print(my_list)


# #### index()

# In[60]:


my_list.index('RCB') #fetch index for any element/item in the list


# ![image.png](attachment:image.png)

# - `index()` returns the first index of the value
# - List can contain duplicate items / elements

# #### Append the two given lists
# 

# In[104]:


my_num1= [1,2,3,4,5,6]
my_num2= [99,98,97,96,94]


# #### Concatenation

# In[62]:


my_list_final = my_num1 + my_num2 #'+' means concatenation of two lists basically appending


# In[63]:


my_list_final


# In[64]:


x=10
y=90
x+y #addition


# - append() method: to add a single element at the end of the list
# -  extend() method: to add multiple elements at the end of the list 
# -  insert() method: to insert an element at the specified **index** position
#     The insert() method takes two arguments, the first is the index at which <br> the element is to be inserted, and the second is the value/ element to be inserted.

# #### append()

# In[69]:


my_num1


# In[70]:


my_num1.append(7)


# In[71]:


my_num1


# In[74]:


my_num1.append(8,9,10)  #takes single argument and can not add more than one element to the list at once


# In[75]:


my_num1.append([8,9,10]) #nested list


# In[76]:


my_num1


# #### extend()

# In[90]:


odd_num=[1,3,5,7,9]
even_num=[2,4,6,8,10]


# ##### Append even numbers after the odd numbers

# In[79]:


odd_num.extend(even_num)


# In[80]:


odd_num


# #### insert()

# In[91]:


even_num


# In[92]:


even_num.index(8)


# In[102]:


even_num.insert(4,999999) #inserted '999999' at the postion #4
even_num


# In[97]:


even_num


# ### Deleting / Removing List elements in Python

# - We can delete the list or delete the element(s) from the list using below functions:

# In[110]:


even_num= [2,4,6,8,10]
print(even_num)


# In[109]:


del even_num #del keyword can delete the whole list from the memory


# In[108]:


even_num


# In[118]:


even_num


# #### using `del` method, a single element at a specific position can also be deleted

# In[119]:


even_num


# In[116]:


del even_num[4] #index position
print(even_num)


# In[114]:


del even_num[6]


# ### H/W Try deleting multiple elements from the list using `del` method

# #### There are three methods for deletion
# `remove()`,  `pop()` , `clear()`

# In[123]:


even_num= [2,4,6,8,10,12,14,16,18,20,12]
print(even_num)


# #### remove()

# - remove() deletes the specific element

# In[126]:


even_num.remove(12) #removes the element 12 from the list #deletes the first occurence of the element # one element at a time


# In[125]:


even_num


# #### pop()

# - pop() method takes the index as an argument and deletes the element at that index & **returns the deleted item**
# - If the index is not given, pop() deletes the last element by default

# In[145]:


num_list = [1,2,3,4,7,99,100,200]
num_list.index(99)


# In[140]:


num_list


# In[141]:


#### Delete 99 from the list
num_list.pop()


# In[142]:


num_list


# In[143]:


num_list.pop(5)


# In[144]:


num_list


# #### clear()
# `pro tip`

# ### Q. What's the difference between `del` and `clear`

# In[146]:


num_list


# In[147]:


num_list.clear() #it deletes all the elements in the list but not the list from the memory => you get an empty list


# In[148]:


num_list


# In[150]:


id(num_list) #identity of the list


# #### In SQL===> Truncate (Clear) & delete (del) the tables

# #### reverse()

# In[153]:


odd_num


# In[154]:


odd_num.reverse()


# In[155]:


odd_num


# #### sort()

# In[156]:


num_list=[1,4,99,100,0.5,300]


# In[158]:


num_list.sort() #by default => ascending  => Low to High 


# In[159]:


num_list 


# `ascending` => low to high

# In[160]:


num_list.sort(reverse=True) # For descending use reverse=True


# In[161]:


num_list


# `descending` => high to low

# ## List Copies & Idenitity Operators

# In[186]:


list_1 = [1,2,3,4,5,6,7,8,9,10]
print(id(list_1))


# In[187]:


list_2 = [1,2,3,4,5,6,7,8,9,10]
print(id(list_2))


# In[188]:


list_1 == list_2  ##Equal operator compares the lists values index wise


# In[189]:


id(list_1)==id(list_2) #Because lists are mutable


# `list_1` and `list_2` refer to two different objects in the memory

# In[190]:


x=10 
y=10
print(x==y)
print(id(x)==id(y)) #variables x and y are having int data types. Unlike lists, they are immutable


# In[191]:


list_3=list_1.copy()
print(id(list_3))


# In[192]:


list_4=list_1
print(id(list_4)) #same


# ![image.png](attachment:image.png)

# In[193]:


print(id(list_1), id(list_2), id(list_3), id(list_4))


# In[194]:


list_4[0]=99999


# In[195]:


list_4


# In[196]:


list_1


# In[197]:


x=[]


# In[198]:


id(x)


# In[199]:


hex(id(x))

Initializing a List:
Initializing a list means assigning initial values to the list. It is the process of giving the list an initial state by populating it with values.
# # Welcome to Python Basics - `Day#05`
# `Instructor - APC`

# ### Strings

# In[1]:


my_text = "Welcome to Basic Python course"
print(my_text)
print(type(my_text))
my_num = '100'
print(my_num)
print(type(my_num))


# - It is a collection of one or more characters put in a single / double / triple single or double quotes
# - In Python, there is no `character` data type

# In[2]:


'APC' #single quotes


# In[3]:


"APC" #double quotes


# In[4]:


''' APC''' #triple quotes (single)


# In[5]:


""" APC """ #triple quotes (double)


# In[6]:


my_text


# In[7]:


len(my_text) #count of letters including space


# In[10]:


my_num


# In[11]:


len(my_num)


# In[1]:


my_list = [10, 20, "APCDDDDDD"]
len(my_list)


# In[2]:


len(my_list[0])


# In[17]:


len(my_list[2])


# In[18]:


len(my_list[0])


# In[19]:


def count_digits(number):
    num_str = str(number)
    print(len(num_str))   


# In[21]:


count_digits(100000000000000000)


# In[22]:


my_num=1000
len(my_num)


# In[23]:


my_num_str=str(my_num) #Explicit Typecasting
len(my_num_str)


# **Python strings are `immutable`

# In[24]:


my_last_name='Pushkat'
print(my_last_name)


# `Want to replace t with r`

# In[29]:


my_last_name[6]='r' #str object can not be mutated


# In[30]:


my_word= 'apple'
my_word[2]


# In[31]:


my_last_name.replacE#replace can be used in this scenario


# In[32]:


dir(str)


# #### Most of the above methods are useful when you are doing NLP/Text Mining part of `Text Analytics`

# #### del

# In[33]:


del my_last_name #delete from the memory


# In[34]:


my_last_name


# ### Create a custom primary key which is combination of multiple columns

# ![image.png](attachment:image.png)

# In[35]:


SKU_ID = "SKU_12345"
SITE_ID = "BLR_001"
CUST_ID ="AKASH_007"


# In[36]:


SKU_ID + SITE_ID + CUST_ID #Concatenation of strings


# In[39]:


SKU_ID + "_"+ SITE_ID +  "_"+CUST_ID #Concatenation of strings


# #### In Pandas

# In[ ]:


df['Primary_Key'] = df['SKU_ID'] + "_" + df['SITE_ID']+ "_"+ df["CUST_ID"] #In Pandas dataframe


# In[40]:


my_num=100
print(my_num*5)


# In[4]:


my_text= "APC"
print(my_text*5)


# In[44]:


my_text= "APC"
my_text


# In[45]:


my_text*5


# In[46]:


2+3


# ### Must Know String Functions

# #### upper() & lower()

# `upper()`: converts the string to uppercase
# 
# `lower()`: converts the string to lowercase

# In[53]:


my_string = 'AkAsh pUshkar'


# In[54]:


my_string.upper() #all capital


# In[55]:


my_string.lower() #all small


# #### split()

# In[60]:


SKU_ID = "SKU_12345"
SITE_ID = "BLR_001"
CUST_ID ="AKASH_007"


# In[63]:


Primary_Key = SKU_ID + "-"+ SITE_ID +"-" +CUST_ID #Concatenation of strings


# In[64]:


Primary_Key


# ##### Text to columns

# - Python string split() function is used to split a string into the list of strings based on a delimiter.
# - In below example, delimiter used is hyphen (-)

# In[66]:


splitted_String = Primary_Key.split(sep="-")


# In[67]:


splitted_String


# In[68]:


len(splitted_String)


# In[72]:


Primary_Key.split(sep="-")


# In[74]:


Primary_Key.split(sep="-",maxsplit= 1)


# #### strip()

# - Used to trim whitespaces(left trim and right trim ones) from the string object

# In[5]:


greeting = "   Hello All!   "
print(greeting)


# In[8]:


greeting.strip()


# #### find()

# - Python String find() method is used to find the index of a substring in a string.

# In[81]:


sentence = 'Hello, all! How are you guys doing today?'
print(sentence)


# In[82]:


sentence.find("today")


# In[84]:


my_text="'Hello, all! How are you guys doing"
len(my_text)


# #### join()

# - This function returns a new string that is the concatenation of the strings in iterable with string object as a delimiter.

# In[85]:


words=['Hello', 'world', 'how', 'are', 'you']
print(words)


# In[90]:


sentence= '*'.join(words)
print(sentence)


# #### replace()

# - Python string replace() function is used to create a new string by replacing some parts of another string.

# In[91]:


string = 'Hello, World!'
new_string = string.replace("Hello", "Hi")
new_string


# ####  SQL Like Operator

# #### str.contains

# - Check if patterm natches (**Pandas function**)

# In[94]:


string = 'Hello, World!'
'Hello' in string


# #### Reading Assignment: Learn about List Comprehension

# In[96]:


numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers] #list comprehension
print(squared_numbers)


# ## Tuple

# ![image.png](attachment:image.png)

# In[104]:


my_tuple = (1, 2.3, "APC", 1, 10, 99, 99, "APC") #Hetereogeneous
print(my_tuple)
print(type(my_tuple))


# In[105]:


dir(tuple)


# `count()` - gives the count of the specified element
# 
# `index()` - gives the index of the **first** occurence of a specified element

# In[107]:


my_tuple


# In[109]:


my_tuple.count(99)


# In[110]:


my_tuple.index('APC')


# ## Set

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# In[119]:


my_set = set([1, 'APC', 7.9, 'BBC']) #hetereogeneous
print(my_set)
print(type(my_set))


# #### Create set data using {}

# In[121]:


my_set1= {1, 'APC', 7.9, 'BBC', 'APC', 'APC'}
print(my_set1)
print(type(my_set1))


# `observation`: Set can have heterogeneous data types but no duplicate items

# In[122]:


my_set2 = {1,2,3}
print(my_set2)


# In[125]:


my_set1={3, 5, 7, 2, 'ABF' , 'GFH'}
print(my_set1)
print(type(my_set1))


# In[126]:


dir(set)


# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# ### Add and Update set items

# In[132]:


nums = {1,3,5,7,9}
print(nums)


# In[133]:


print(type(nums))


# #### Add

# In[134]:


nums.add(11)


# ![image.png](attachment:image.png)

# In[135]:


print(nums)


# In[140]:


nums.add(7)
nums


# #### update

# In[136]:


nums.update([13,15,17,19,21])


# In[137]:


print(nums)


# In[138]:


nums.update(23,25,27)


# #### Remove an element from the set

# ##### discard()

# `discard`: it removes a specified element from a set. If the element is not present in the set, `discard` does nothing and doesn't raise an error

# In[160]:


nums


# In[161]:


### remove the number 13
nums.discard(13)
print(nums)


# In[162]:


nums.discard(99)
nums


# ##### remove()

# `remove`: it removes a specified element from a set. If the element is not present in the set, `remove` raises an error

# In[163]:


nums.remove(15)
print(nums)


# In[147]:


nums.remove(99)
print(nums)


# ##### pop()

# `pop`: removes and returns an arbitrary element from the set. Since sets are unordered, the specific element that gets removed cannot be determined.
# - if the set is empty, `pop` raises a 'KeyError'

# In[148]:


nums


# In[149]:


nums.pop()


# In[150]:


nums


# In[151]:


nums.pop()


# In[152]:


my_set


# In[153]:


my_set.pop()


# In[156]:


my_set.add("ALPHA")


# In[157]:


my_set


# #### How to remove multiple elements from the set

# In[158]:


set_minus = { 'ALPHA', 'APC', 'BBC'}


# ##### set difference

# In[159]:


my_set - set_minus #base set and subtracting the sey minus


# ### Union, Intersection, Difference, Equality

# In[164]:


a={1,2,3,4,5,6,7}
b = {1,4,99,10}

print('Set a:', a)
print('Set b:', b)


# #### union

# In[168]:


print(a.union(b))


# In[169]:


print(b.union(a))


# #### intersection (common)

# In[170]:


print(a.intersection(b))


# In[167]:


print(b.intersection(a))


# #### difference

# In[172]:


print(b.difference(a)) #elements in Set b but not in Set a


# In[173]:


#### difference
print(a.difference(b)) #elements in Set a but not in Set b


# #### equality of sets

# In[174]:


print('Set a and b are equal or not:', a==b)


# In[176]:


c= {1,4,99,10}


# In[177]:


print('Set b and c are equal or not:', b==c)


# ## Dictionary

# https://www.coin-or.org/PuLP/CaseStudies/a_transportation_problem.html

# - Dicitonary data type is used in one of the very famous optimization libraries **pulp**

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# - Python dictionary is an ordered collection of items / elements
# - It stores elements in key-value pairs
# - Keys are unique identifiers which are associated with values
# - Keys are case sensitive
# - they always exist  in pairs

# ##### Create a dictionary for the number of units of supply for each supply node

# In[179]:


supply = {"A": 1000, "B": 4000}
print(supply)
print(type(supply))


# In[180]:


dir(dict)


# In[181]:


print(supply.keys()) #keys


# In[182]:


print(supply.values()) #values


# In[186]:


supply_updated= {"A": 1000, "B": 4000, "A":2000}
print(supply_updated)


# `observation`: In case, a dictionary has two or more values mapped to the single key, it will show the latest one

# ![image.png](attachment:image.png)

# In[12]:


a = {}
print(type(a))


# In[188]:


b = set()
print(type(b))


# In[23]:


a = {"A":100, "B":1000, "A":100}
b = {100,1000}
print(type(a))
print(type(b))
print(a)


# In[192]:


hex(id(a))  #integer into a hexadecimal string

[] # list
() #tuple
{} #dictionary but can we used to create a set
# In[24]:


a=10
hex(a)

