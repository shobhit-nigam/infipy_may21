#!/usr/bin/env python
# coding: utf-8

# In[1]:


fa = open("books.txt", "r") 


# In[2]:


stra = fa.read(4)


# In[3]:


print(stra)


# In[4]:


stra = fa.read(4)
print(stra)


# In[5]:


fa.tell()


# In[6]:


fa.seek(0)


# In[7]:


stra = fa.readline()


# In[8]:


print(stra)


# In[9]:


fa.seek(0)
stra = fa.read()
print(len(stra))
print(stra)


# In[10]:


stra


# In[11]:


fa.close() 


# In[12]:


with open("books.txt", 'r') as fa:
    stra = fa.read()


# In[13]:


fa.closed


# In[14]:


print("bengaluru\newdelhi")


# In[15]:


print(r"bengaluru\newdelhi")


# In[16]:


help(print)


# In[17]:


strb = r'{}'.format(stra)


# In[18]:


strb


# In[19]:


data = 32
datb = 100


# In[21]:


stra = "a = {} b = {}".format(data, datb)


# In[22]:


print(stra)


# In[23]:


stra


# In[24]:


stra = "a = {0} b = {1} c ={0}".format(data, datb)


# In[25]:


stra


# In[26]:


stra = f"a = {data} b = {datb}" 


# In[27]:


stra


# In[28]:


print(strb)


# In[29]:


strb = r"{}".format(stra)


# In[30]:


stra


# In[31]:


with open("books.txt", 'r') as fa:
    stra = fa.read()


# In[32]:


strb = r"{}".format(stra)


# In[33]:


stra


# In[34]:


strb


# In[35]:


print(strb)


# In[37]:


print(r'%s' python )


# In[38]:


strc = "hi\nhello"
strd = "hi\\nhello"


# In[39]:


print(strc)


# In[40]:


print(strd)


# In[41]:


"""[obja, objb, objc]

[objb, obja, objc] """


# In[ ]:




