#!/usr/bin/env python
# coding: utf-8

# In[3]:


lista = list("hello world")


# In[4]:


lista


# In[5]:


def vowels(ca):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return ca in vowels


# In[6]:


fa = list(filter(vowels , lista))


# In[7]:


print(fa)


# In[8]:


listb = ['', 0, 'hi', 23, None, False, [7, 8, 10], 0]


# In[9]:


listc = [23, listb, lista, "hello"]


# In[10]:


listc


# In[11]:


lista.append('r')


# In[12]:


listc


# In[13]:


listcopy = lista


# In[14]:


lista


# In[15]:


listcopy


# In[16]:


listcopy.sort()
listcopy.remove('l')


# In[17]:


listcopy


# In[18]:


lista


# In[19]:


lista = list("hello world")


# In[20]:


lista


# In[21]:


listcopy = lista.copy()


# In[22]:


# mutables


# In[24]:


listb = ['', 0, 'hi', 23, None, False, [7, 8, 10], 0, []] 


# In[25]:


list(filter(None, listb))


# In[26]:


listx = [4, 7, 12, 5, 9, 11, 3]


# In[27]:


def algo(la):
    return la*2 + 3


# In[28]:


list(map(algo, listx))


# In[29]:


listx = [4, 7, 12, 5, 9, 11, 3]
listy = [11, 17, 27, 13, 21, 25, 9]


# In[30]:


def algo(la, lb):
    return la*2 + lb-1


# In[31]:


list(map(algo, listx, listy))


# In[32]:


def funca(ta, tb):
    print("ta =", ta)
    print("tb =", tb)


# In[34]:


funca(100, 200)


# In[35]:


def funca(ta, tb, *tc):
    print("ta =", ta)
    print("tb =", tb)
    print("tc =", tc)


# In[36]:


funca(100, 200, 300, "hi", [5, 6, 7])


# In[37]:


None()


# In[38]:


varx = None
vary = None


# In[39]:


varx == vary


# In[40]:


id(varx)


# In[41]:


id(vary)


# In[42]:


listb = ['', 0, 'hi', 23, None, False, [7, 8, 10], 0, []] 


# In[43]:


listb[4] == varx


# In[44]:


id(listb[4])


# In[45]:


data = 23


# In[46]:


id(data)


# In[47]:


id(listb[3])


# In[48]:


strc = ''


# In[49]:


type(strc)


# In[50]:


len(strc)


# In[51]:


# python docs 


# In[52]:


def algo(la):
    return la*2 + 3

map(algo, listx)

list(map(lambda la: la*2+3 , listx))


# In[54]:


listx


# In[56]:


list(map(lambda x, y : x+y , listx, listy))


# In[63]:


list(map(lambda x, y : x+y if (x+y)>16 else None, listx, listy))


# In[64]:


def funca(x, y):
    if (x+y)>16:
        return x+y
    else:
        return None


# In[66]:


list(filter(lambda x: x>10, listx))


# In[67]:


list(filter(lambda x, y : x>y, (listx, listy))


# In[72]:


listx = [1, 2, 3, 4, 5, 6]
listy = [10, 20, 30, 40, 50, 60, 70, 80, 90]

def algo(la, lb):
    return la+lb


# In[73]:


list(map(algo, listx, listy)) 


# In[77]:


listx = [1, 2, 3, 4, 5, 6]
listy = [20, 120, 300, 410, 50, 60, 70, 180, 90, 100, 110]

def algo(la, lb):
    return la+lb


# In[78]:


list(map(algo, listy, listx)) 


# In[79]:


# numpy pandas


# In[80]:


# matplotlib  matlab 


# In[82]:


def funcx(n):
    yield n

    n = n+1
    yield n

    n = n+1
    yield n


# In[83]:


print(funcx(3))


# In[84]:


x = funcx(3)


# In[85]:


next(x)


# In[87]:


next(x)


# In[88]:


next(x)


# In[89]:


next(x)


# In[90]:


# __iter__()    __next__()


# In[91]:


for val in funcx(4):
    print(val)


# In[92]:


for i in range(4):
    print(i)


# In[93]:


for x in listx:
    print(x)


# In[94]:


def funca(ta, tb, *args, **kwargs):
    print("ta =", ta)
    print("tb =", tb)
    print("args =", args)
    print("kwargs =", kwargs)


# In[95]:


funca(100, 200, 300, "hi", [5, 6, 7], country='norway', region='scandanavian')


# In[96]:


ga = 100

def funcg():
    print("ga in func =", ga)


# In[97]:


funcg()


# In[98]:


ga = 100

def funcg():
    la = 33
    print("ga in func =", ga)


# In[99]:


la


# In[100]:


ga = 100

def funcg():
    la = 33
    ga = 33
    print("ga in func =", ga)


# In[101]:


ga


# In[102]:


funcg()


# In[103]:


ga


# In[104]:


ga = 100

def funcg():
    global ga
    la = 33
    ga = 33
    print("ga in func =", ga)


# In[105]:


ga


# In[106]:


funcg()


# In[107]:


ga


# In[108]:


ga = 100

def funcg():
    ga = ga + 10
    print("ga in func =", ga)


# In[109]:


funcg()


# In[111]:


print(funcg.__doc__)


# In[112]:


# annotations 


# In[113]:


def funcs(la, lb) -> str:
    return "hello"


# In[114]:


val = funcs(10, 20)


# In[115]:


print(val)


# In[116]:


def funcs(la, lb) -> str:
    return 100


# In[117]:


val = funcs(10, 20)
print(val)


# In[118]:


type(val)


# In[119]:


def funcs(la, lb:int) -> str:
    return 100


# In[120]:


val = funcs(10, 'ii')
print(val)


# In[121]:


funcs.__annotations__


# In[122]:


help(funcs)


# In[123]:


import inspect


# In[124]:


help(inspect)


# In[126]:


inspect.getsource(len)


# In[127]:


def funca(la, lb):
    lc = la+lb
    return lc


# In[128]:


inspect.getsource(funca)


# In[129]:


import time


# In[130]:


inspect.getsource(time) 


# In[132]:


inspect.getsourcelines(__builtins__.print)


# In[133]:


get_ipython().run_line_magic('pinfo2', 'time')


# In[134]:


import pandas


# In[135]:


inspect.getsource(pandas)


# In[ ]:




