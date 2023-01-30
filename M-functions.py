#!/usr/bin/env python
# coding: utf-8

# In[3]:


x = 1
y = 2
x+y 


# In[5]:


x


# In[13]:


def add_numbers(x,y,z=None):
    if (z == None):
        return x+y
    else:
        return x+y+z

print(add_numbers(1,2))
print(add_numbers(1,2,3))


# In[18]:


def add_numbers(x,y,z=None,flag=False):
    if(flag):
        print('Flag is true!')
    if(z==None):
        return x+y
    else:
        return x+y+z
print(add_numbers(1,2,flag=True))    


# In[20]:


def add_numbers(x,y):
    return x+y
a = add_numbers
a(1,2)

