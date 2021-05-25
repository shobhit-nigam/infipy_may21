#!/usr/bin/env python
# coding: utf-8

# In[1]:


varx = 10
vary = 20 

print(type(varx))


# In[2]:


ba = True

print(type(ba))


# In[3]:


varx = "india"

print(type(varx))


# In[4]:


def varx():
    print("greetings ")


# In[6]:


print(type(varx))


# In[7]:


varx()


# In[9]:


ca = 7 + 8j


# In[10]:


print(type(ca))


# In[12]:


ca + ca


# In[13]:


import os

# os.system('cls')
# os.system('clear')


# In[15]:


fa = 32.45

print(type(fa))


# In[16]:


ia = int(fa)

print(type(ia))


# In[18]:


y = varx


# In[19]:


varx()


# In[20]:


y()


# In[21]:


print("hello world")


# In[22]:


rakshit = print


# In[23]:


rakshit("let the force be with you")


# In[24]:


# display = print


# In[26]:


# print("hi") + print("hello")


# In[27]:


def outer():
    print("outer")
    def inner():
        print("inner")
    print("outer again")


# In[28]:


outer() 


# In[29]:


def outer():
    print("outer")
    def inner():
        print("inner")
    print("outer again")
    return inner


# In[30]:


x = outer
x = outer() 


# In[31]:


x()


# In[32]:


def outer():
    print("outer")
    def inner():
        print("inner")
    print("outer again")
    return inner()


# In[33]:


sa = None


# In[34]:


print(type(sa))


# In[35]:


def funcb(la, lb):
    lc = la+lb
    return lc, lc*2


# In[37]:


ra , rb = funcb(10, 20)


# In[38]:


print("ra =", ra)
print("rb =", rb)


# In[39]:


x, y , z = 100, 200, "hello"


# In[40]:


x, y  = 100, 200, "hello" 


# In[41]:


x, y , z, w = 100, 200, "hello"


# In[42]:


ra , rb , rc = funcb(10, 20)


# In[43]:


x, y , z = 100, 200, "hello"


# In[44]:


print(type(y))


# In[46]:


x = 100, 200, "hello"


# In[47]:


print(type(x))


# In[48]:


print(x)


# In[49]:


x, y, z = 100


# In[50]:


x = y = z = 100


# In[51]:


y = 100+3


# In[52]:


print(x)


# In[53]:


print(y)


# In[57]:


ca = "hello"
cb = 'h'


# In[55]:


len(ca)


# In[56]:


len(cb)


# In[58]:


print(type(ca))


# In[59]:


print(type(cb))


# In[60]:


stat = "hi'


# In[61]:


stat = "she does'nt love me anymore"


# In[62]:


stat = 'i like "sweets" '


# In[63]:


stat.upper()


# In[64]:


stat.isalpha()


# In[65]:


help(str)


# In[69]:


get_ipython().run_line_magic('pinfo', 'vary.from_bytes')


# In[70]:


fa.is_integer()


# In[71]:


i = 20


# In[72]:


import os as datetime


# In[73]:


datetime.getcwd()


# In[74]:


#datetime.mkdir()


# In[75]:


datetime.datetime.now()


# In[76]:


import datetime


# In[77]:


datetime.getcwd()


# In[ ]:




