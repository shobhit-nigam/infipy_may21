#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os


# In[2]:


os.getcwd()


# In[3]:


"\\newfolder\\tablet"


# In[4]:


import time


# In[6]:


print("hi")
time.sleep(5)
print("hello")


# In[7]:


import datetime


# In[8]:


today = datetime.date.today()


# In[9]:


print(today)


# In[10]:


today.year


# In[12]:


now = datetime.datetime.now()


# In[13]:


now.strftime("%H:%M")


# In[14]:


now.strftime("%d:%m:%Y %H:%M")


# In[15]:


now.strftime("%d:%m:%y %H:%M")


# In[16]:


import sys


# In[17]:


sys.path


# In[19]:


timea = datetime.date(year=2019, month=7, day=18)
timeb = datetime.date(year=2021, month=5, day=24)


# In[21]:


timec = timeb - timea


# In[22]:


print(timec)


# In[23]:


from colours import blue, green


# In[24]:


blue()


# In[25]:


yellow()


# In[26]:


green()


# In[27]:


yellow()


# In[30]:


from datetime import datetime as d


# In[31]:


now = datetime.datetime.now()

now = d.now()


# In[35]:


print(type(datetime.datetime))


# In[36]:


from time import sleep


# In[37]:


print(type(sleep))


# In[38]:


from matplotlib import pyplot


# In[39]:


import matplotlib.pyplot


# In[40]:


import colours


# In[41]:


colours.red()


# In[42]:


import colours


# In[43]:


colours.blue()


# In[44]:


colours.red()


# In[45]:


import importlib


# In[46]:


importlib.reload(colours)


# In[47]:


colours.red()


# In[48]:


# os.setuid()


# In[49]:


import one


# In[50]:


import sys


# In[51]:


sys.path


# In[52]:


sys.path.append('/Users/shobhit/Desktop/infineon/')


# In[53]:


sys.path


# In[54]:


import one


# In[55]:


os.getenv('USER')


# In[56]:


os.getenv('PATH')


# In[57]:


import pandas


# In[58]:


p = '/Users/shobhit/Desktop/infineon/'


# In[59]:


p in sys.path


# In[ ]:




