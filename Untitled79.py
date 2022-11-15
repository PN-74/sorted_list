#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Python Candidates - Question 1

You will have a number of elements and in the next n lines element of a list. You have to create a list from the given strings. You have to sort the list based on 2nd last character of a string.

For example: given list = ['great','hello','hiyo','abc'] so your output_dictionary should be ['great', 'abc', 'hello','hiyo']



# In[1]:


# ANSWER

list1 = ['great','hello','hiyo','abc']
list1.sort(key=lambda item:item[-2])
print(list1)
['great', 'abc', 'hello', 'hiyo']


# In[ ]:




