#!/usr/bin/env python
# coding: utf-8

# ### 1
# 
# - Convert all characters of the word "PYTHON" to its decimal equivalent and then store them.
# - Convert all the decimal equvalents back to characters 
# 
# 

# In[56]:


# first printing PYTHON word into its decimal equivalent
s = "PYTHON"
dec_eq=[ord(p) for p in s] #here we are uing ord function to make string into it's decimal equivalent
print(dec_eq)

# now printing the PYTHON word from its decimal equivalent 
char_eq=[chr(c) for c in dec_eq] #here we are using chr function to make decimal equivalent back to characters
print(char_eq)


# ### 2
# - Raise 2 to the power 10

# In[66]:


x=2**10
print("value:",x) 
#print(pow(2,10))  we can also use the pow(base,exp) function here


# ### 3
# 
# - From the given list, starting from Japan, print alternate elements
# - From the given list, print element at indexes 1,4,5,8 (**Hint**: Use for loop or list comprehension)

# In[34]:



#Part 1
list1=["India", "Japan","Singapore","China","Australia","Africa","Dubai","France","Italy","Germany"]
count=0
for i in list1:   # here we are using the for loop to iterate through the list and make the count increase
    count=count+1
    print(list1.pop(count)) #here we are printing out alternate index courtries


# In[1]:


#Part 2
list1=["India", "Japan","Singapore","China","Australia","Africa","Dubai","France","Italy","Germany"]
list1 = [x for (i,x) in enumerate(list1) if i not in (0,2,3,6,7,9)] #here the enumerate function is used to print out indexes 1,4,5,8
print(list1)


# ### 4
# 
# - From the given list, extract the "Hex" and print it

# In[45]:



list2=[22,[4, [True, False], 6, 8], [888, 999,[111,222,["Hex"]]] ]
list2[2][2][2] #here by using indexing we are printing out the Hex


# ### 5
# 
# - From the given dictionary, fetch the keyword "TOPD"

# In[54]:



dict1={"Tevatron":["Technologies","Pvt","Ltd",{"Domains":["Embedded","IoT","AI","ML"],"Projects":["inhouse","TOPD"]}]}
list1=dict1["Tevatron"] #here we are indexing the list from the dict1
dict2=list1[3] #here we are indexing the dict2 from the list1
list2=dict2["Projects"] # again indexing the list in it
list2[1] # and finally printing out the desired output


# ### 6
# There are 3 height categories
# 
# **167 and below  =**    Short <br>
# **168 to 182     =**    Average <br>
# **182 and above  =**    Tall<br>
# 
# Write a programe which gets the input from user and prints if the category the person fits in
# 
# **Hint**: Use function input()

# In[61]:


h=input("Enter height: ") # user input
height=int(h)
if ((height<=167) & (height>0)): # we are using the if, elif condition to make the desired conditions
    print("Short")
elif ((height>168) & (height<182)): # we are also using & to satisfy the both conditions
    print("Average")
elif (height>=182):
    print("Tall") 
else:
    print("Invalid Input")


# ### 7
# 
# Using maximum 2 lines of code, generate all upper case alphabets
# 
# **Hint**: Refer ASCII Table

# In[73]:


alphabet=("a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z") # here we are defining all the alphabets
alphabet.upper() # now by using upper function we are make all alphabets in uppercase


# ### 8
# 
# Generate integers between (100 and 200) both inclusive, using NumPy

# In[90]:


import numpy as np  # importing numpy 
arr=np.arange(100,201) # we are making the array by using arange function 
arr


# ### 9
# 
# Print all even integers from the array created in Task8

# In[91]:


count=0
for i in arr: # here we using the for loop to iterate through the array
    count=count+1 # increasing the count every time loop iterate
    if count%2 ==0: # making condition only for even numbers
        print(arr[count])


# ### 10
# 
# Print all 100 values from Standard Normal Distribution

# In[99]:


val=np.random.randn(100) # making the random array of 100 values by using random.randn() function
print(val)


# ### 11
# 
# Create a NumPy array of random number, whose dimension attribute is equal to 4

# In[113]:


arr=np.random.rand(2,2,2,2) #creating the random array of dimension attribute 4
print(arr)
#to show thw dimension attribute
print("Dimension attribute", arr.ndim)


# ### 12
# 
# Create an NumPy array of 100 values evenly spaced between 10 and 20

# In[114]:


np.linspace(10,20,100) # here we are creating  an array by using linspace() function to make values evenly spaced


# ### 13
# 
# Create a NumPy array of shape 5x5 and print the last 3 rows

# In[124]:


arr=np.arange(1,26).reshape(5,5) #here by using the arange() function and reshape() function we are making a 5*5 array
arr[2:5] # by using slicing we are printing out the last 3 rows


# ### 14
# 
# Using the array created above in Task13, Print the first 2 columns

# In[131]:


arr[:,0:2] # here we are using the indexing to print out he first 2 columns


# ### 15
# 
# Create an array of 25 random values
# - Find the sum of all elements
# - Print the element with maximum value and minimum value

# In[145]:


arr1=np.random.randint(1,26,size=25) # here we are usig random.randint() function to make random integer values array 
print("Sum:",arr1.sum()) # here printing the sum by using sum() function
print("Maximum value:",arr1.max()) # here printing the max by using max() function
print("Minimum value:",arr1.min()) # here printing the min by using min() function


# 16
# 
# In the array created above, print columns with indexes 1,3,4 without directly indexing them

# In[62]:


import numpy as np
arr=np.arange(1,26).reshape(5,5) # here making the array by using arange() function and reshaping it to 5*5 array
print(arr)
arr = [x for (i,x) in enumerate(arr) if i not in (0,2)] 
print(arr)


# ### 17
# Read car_sales.csv

# In[9]:


import pandas as pd
r=pd.read_csv("car_sales.csv") # reading the csv file using pd.read_csv()
r


# ### 18
# Sort data frame in ascending order of the Price column

# In[15]:


r.sort_values("Price") # using sort_values() function, sorting the values on basis of Price


# ### 19
# Print number of unique car manufacturers in the data

# In[24]:


print("Number of unique values:",r["Manufacturer"].nunique()) # printing out the number of unique values by using nunique() function


# ### 20
# Print the maximum Wheelbase from the data

# In[23]:


print("Maximum Wheelbase:",r["Wheelbase"].max()) # printing out the maximum wheelbase using max() function


# ### 21
# Print the car Model which has maximum Wheelbase

# In[36]:


c=r.sort_values("Wheelbase",ascending=False) # here we are sorting the values on basis of Wheelbase using sort_values() function
car_model=c["Model"] 
car_model[35] # printing out the car model with max Wheelbase using indexing


# ### 22
# 
# Print the Details of car with maximum passenger capacity

# In[50]:


max_pass_cap=r.sort_values("Passengers",ascending=False) # here we sorting the values on basis of Passengers 
car_details=max_pass_cap.loc[16] # here we are finding all the car details of max passenger capacity using .loc[] 
print(car_details)

