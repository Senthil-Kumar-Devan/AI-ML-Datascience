#!/usr/bin/env python
# coding: utf-8

# # Exercise 1: Write a function to sort the list based on the first letter of the second element
# lst=[(19542209, "New York") ,(4887871, "Alabama"), (1420491, "Hawaii"), (626299, "Vermont"), (1805832, "West Virginia"), (39865590, "California")]

# In[39]:


lst=[(19542209, "New York") ,
     (4887871, "Alabama"), (1420491, "Hawaii"), (626299, "Vermont"), 
     (1805832, "West Virginia"), (39865590, "California")]
"""
Signature: lst.sort(*, key=None, reverse=False)
Docstring:
Sort the list in ascending order and return None.
"""
print("Original List: \n", lst)

#Sort function to sort the first letter of the second element in list
def sorter(sample_list):
    sample_list.sort(key=lambda l:l[1])
    return sample_list

print("\nResults of Sorting first letter of the 2nd element in the list:\n" ,sorter(lst))


# # Exercise 2: Write a function to sort the list based on the last letter of the second element¶
# Use list from previous question

# In[42]:


lst_Ex2=[(19542209, "New York") ,
     (4887871, "Alabama"), (1420491, "Hawaii"), (626299, "Vermont"), 
     (1805832, "West Virginia"), (39865590, "California")]
"""
Signature: lst.sort(*, key=None, reverse=False)
Docstring:
Sort the list in ascending order and return None.
"""

print("Original List: \n", lst_Ex2)

#Sort function to sort the last letter of the second element in list
def sorter(sample_list):
    sample_list.sort(key=lambda l:l[-1])
    return sample_list

print("\nResults of Sorting last letter of the 2nd element in the list:\n" ,sorter(lst_Ex2))


# # Exercise 3: Create a range from 1 to 8 merge the given list and together to create a new list of tuples.
# lst1=["Energy", "Agriculture", "Industry", "Technology", "Finance", "Forestry", "Transport"]

# In[58]:


lst1=["Energy", "Agriculture", "Industry", "Technology", "Finance", "Forestry", "Transport"]

'''
Init signature: range(self, /, *args, **kwargs)
Docstring:     
range(stop) -> range object
range(start, stop[, step]) -> range object
'''
lst2 = range(1,8)

'''
Init signature: map(self, /, *args, **kwargs)
Docstring:     
map(func, *iterables) --> map object

Make an iterator that computes the function using arguments from
each of the iterables.  Stops when the shortest iterable is exhausted.
'''
merged_list = list(map(lambda l1,l2: (l1,l2), lst1, lst2))

print("Merge list and range to list of Tuples: \n",merged_list)


# # Exercise 4: Write a function and create a list consisted of the number of occurence of letter: a (all a's).
# lst1=["Antartica", "America", "Armania", "Australia", "Albania", "Afganistan","Alaska"]

# In[73]:


lst1=["Antartica", "America", "Armania", "Australia", "Albania", "Afganistan","Alaska"]
#using anonymous lambda function
list(map(lambda x: x.lower().count("a"), lst1))


# # Exercise 5: Write a function filter all the vowels in a given string using filter.
# str1="Inceptz is one of the best institutes to read data science in chennai"

# In[43]:


str1="Inceptz is one of the best institutes to read data science in chennai"

'''
Init signature: filter(self, /, *args, **kwargs)
Docstring:     
filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
'''
def vowfinder(orgString):
    vowels = "aAeEiIoOuU"
    
    for lttr in orgString:
        if lttr in vowels:
            return True
        else:
            return False

vowels = "aAeEiIoOuU"
print(list(filter(vowfinder, str1)))


# # Exercise 6: Write a function to create a list as the square of elements from the given list if the square is greater than 60
# lst1=[5, 6, 7 , 8, 9, 10, 12, 14]

# In[72]:


lst1=[5, 6, 7 , 8, 9, 10, 12, 14]

#Square the List
sq_outList = list(map(lambda x: x**2,lst1))
#Check if Squared list is > 60
output_List = list(filter(lambda x: x>60, sq_outList))
#Pirnt
print(output_List)


# # Exercise 7: take the words given below as list and write a function and use reduce to make it a sentenc

# In[67]:


sen_list = ["Inceptz","provides","the","best","inclass","trainings","and","is","the","best"]
'''
Docstring:
reduce(function, sequence[, initial]) -> value

Apply a function of two arguments cumulatively to the items of a sequence,
from left to right, so as to reduce the sequence to a single value.
For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
of the sequence in the calculation, and serves as a default when the
sequence is empty.
'''
from functools import reduce as rd

rd(lambda x,y: x+" "+y,sen_list)

