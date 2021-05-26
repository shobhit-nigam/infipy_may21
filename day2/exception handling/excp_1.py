#!/usr/bin/env python
# coding: utf-8

# In[1]:


lista = ['aa', 'bb', 'yy', 'rr', 'ee', 'zz']


# In[2]:



i = int(input())
print(lista[i])


# In[3]:


i = int(input())
print(lista[i])


# In[5]:


try:
    i = int(input())
    print(lista[i])
except IndexError:
    print("wrong index, resetting it to zero")
    i = 0
    print(lista[i])


# In[6]:


True = 11


# In[7]:


print = 11


# In[8]:


type(print)


# In[9]:


print("hello")


# In[10]:


# print = __builtins__.print

del print


# In[11]:


print("hello")


# In[13]:


try:
    i = (input())
    print(lista[i])
except IndexError:
    print("wrong index, resetting it to zero")
    i = 0
    print(lista[i])


# In[14]:


try:
    i = (input())
    print(lista[i])
except IndexError:
    print("wrong index, resetting it to zero")
    i = 0
    print(lista[i])
except TypeError:
    print("index not given as int, resetting it to zero")
    i = 0
    print(lista[i])


# In[17]:


try:
    i = (input())
    print(lista[i])
except IndexError:
    print("wrong index, resetting it to zero")
    i = 0
    print(lista[i])
except TypeError:
    print("index not given as int, converting to int")
    i = int(i)
    print(lista[i]) 


# In[18]:


try:
    i = (input())
    print(lista[i])
except IndexError:
    print("wrong index, resetting it to zero")
    i = 0
    print(lista[i])
except TypeError:
    print("index not given as int, converting to int")
    i = int(i)
    print(lista[i]) 


# In[19]:


try:
    i = int(input())
    print(listb[i])
except IndexError:
    print("wrong index, resetting it to zero")
    i = 0
    print(lista[i])
except TypeError:
    print("index not given as int, converting to int")
    i = int(i)
    print(lista[i]) 


# In[20]:


try:
    i = int(input())
    print(listb[i])
except IndexError:
    print("wrong index, resetting it to zero")
    i = 0
    print(lista[i])
except TypeError:
    print("index not given as int, converting to int")
    i = int(i)
    print(lista[i]) 
except:
    print("something went wrong")


# In[21]:


try:
    i = int(input())
    print(listb[i])
except:
    print("something went wrong")
except IndexError:
    print("wrong index, resetting it to zero")
    i = 0
    print(lista[i])
except TypeError:
    print("index not given as int, converting to int")
    i = int(i)
    print(lista[i]) 


# In[22]:


try:
    try:
        i = int(input())
        print(listb[i])
    except NameError:
        print("oops, the variable name is wrong")
except IndexError:
    print("wrong index, resetting it to zero")
    i = 0
    print(lista[i])
except TypeError:
    print("index not given as int, converting to int")
    i = int(i)
    print(lista[i]) 
except:
    print("something went wrong")


# In[23]:


try:
    try:
        i = int(input())
        print(lista[i])
    except NameError:
        print("oops, the variable name is wrong")
except IndexError:
    print("wrong index, resetting it to zero")
    i = 0
    print(lista[i])
except TypeError:
    print("index not given as int, converting to int")
    i = int(i)
    print(lista[i]) 
except:
    print("something went wrong")


# In[24]:


try:
    funca()
except:
    pass


# In[26]:


try:
    i = int(input("enter only positive values:\n")) 
    if i < 0:
        raise ValueError("positives only please")
except ValueError as x:
    print(x)


# In[27]:


try:
    i = int(input("enter only positive values:\n")) 
    if i < 0:
        raise ValueError("positives only please")
except ValueError as x:
    print(x)


# In[28]:


try:
    i = int(input("enter only positive values:\n")) 
    if i < 0:
        raise ValueError(i)
except ValueError as x:
    print(x)


# In[29]:


# Exception


# In[30]:


try:
    i = int(input())
    print(lista[i])
except IndexError:
    print("wrong index, resetting it to zero")
    i = 0
    print(lista[i])
else:
    print("else block executes")
finally:
    print("finally block executes")
    
print("code continues")


# In[31]:


try:
    i = int(input())
    print(lista[i])
except IndexError:
    print("wrong index, resetting it to zero")
    i = 0
    print(lista[i])
else:
    print("else block executes")
finally:
    print("finally block executes")
    
print("code continues")


# In[32]:


try:
    i = int(input())
    print(lista[i])
except IndexError:
    print("wrong index, resetting it to zero")
    i = 0
    print(lista[i])
else:
    print("else block executes")
finally:
    print("finally block executes")
    
# statements 
print("code continues")


# In[33]:


int('6')


# In[34]:


int("'6'")


# In[35]:


class AppExcept(Exception):
    pass


# In[36]:


import sys 


# In[39]:


try:
    lista[23]
except:
    print("handled")
    print(sys.exc_info())


# In[40]:


try:
    lista[23]
except:
    print("handled")
    print(sys.exc_info()[1])


# In[ ]:




