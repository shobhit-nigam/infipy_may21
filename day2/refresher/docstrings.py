#!/usr/bin/env python
# coding: utf-8

# In[5]:


listx = ['ss', 'tt']


# In[6]:


def funca(lx):
    listx = ['55', '44']
    listx.append('77')
    print(listx)


# In[7]:


funca(listx)


# In[8]:


listx


# In[9]:


stra = "hello"


# In[10]:


strb = "hello
there"


# In[11]:


strb = """hello
there"""


# In[12]:


print(strb)


# In[13]:


strb


# In[14]:


# docstrings 


# In[15]:


" hhhh"


# In[17]:


def algo(la, lb):
    "function is used to add two numbers in the form of ax+b+c"
    return la*3 + lb + 10


# In[18]:


print(type(algo))


# In[19]:


print(algo.__doc__)


# In[20]:


def algo(la, lb):
    """function is used to add two numbers 
    in the form of ax+b+c"""
    return la*3 + lb + 10


# In[21]:


print(algo.__doc__)


# In[22]:


help(algo)


# In[24]:


class X:
    "adca"
    
    pass


# In[25]:


help(print)


# In[26]:


help(str.upper)


# In[27]:


print(print.__doc__)


# In[28]:


help(algo)


# In[29]:


algo.__doc__ = "adfd"


# In[30]:


help(algo)


# In[31]:


help(str.upper)


# In[32]:


import os


# In[33]:


help(os.getcwd)


# In[ ]:




