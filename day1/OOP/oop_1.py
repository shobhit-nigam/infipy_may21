#!/usr/bin/env python
# coding: utf-8

# In[2]:


class bank:
    cid = 0
    opening_balance = 0
    current_balance = 0
    name = ""
    
    def update(i, c, n):
        cid = 0
        current_balance = c + opening_balance
        name = ""    
    
    def info():
        print("hello ", name)
        print("your current balnce is ", current_balance)
        
    def deposit(amt):
        current_balance = current_balance + amt
        print("deposited successfully")
        
    def withdraw(amt):
        if current_balance < amt:
            print("insufficient balance")
        else:
            current_balance = current_balance - amt
            print("withdrawn successfully")
            print("your current balnce is ", current_balance)
            


# In[5]:


obja = bank()
objb = bank()


# In[4]:


obja.current_balance


# In[6]:


obja.info()

#   obja.info() -->  bank.info()
#               -->  bank.info(obja) 


# In[10]:


class bank:
    cid = 0
    opening_balance = 0
    current_balance = 0
    name = ""
    
    def update(i, c, n):
        cid = 0
        current_balance = c + opening_balance
        name = ""    
    
    def info(ttt):
        print("hello ", ttt.name)
        print("your current balance is ", ttt.current_balance)
        
    def deposit(amt):
        current_balance = current_balance + amt
        print("deposited successfully")
        
    def withdraw(amt):
        if current_balance < amt:
            print("insufficient balance")
        else:
            current_balance = current_balance - amt
            print("withdrawn successfully")
            print("your current balnce is ", current_balance)
            


# In[11]:


obja = bank()
objb = bank()


# In[12]:


obja.info()


# In[13]:


obja.current_balance = 100


# In[14]:


obja.info()


# In[15]:


objb.info()


# In[16]:


class bank:
    cid = 0
    opening_balance = 0
    current_balance = 0
    name = ""
    
    def update(self, i, c, n):
        self.cid = i
        self.current_balance = c + self.opening_balance
        self.name = n    
    
    def info(self):
        print("hello ", self.name)
        print("your current balance is ", self.current_balance)
        
    def deposit(self, amt):
        self.current_balance = self.current_balance + amt
        print("deposited successfully")
        
    def withdraw(self, amt):
        if self.current_balance < amt:
            print("insufficient balance")
        else:
            self.current_balance = self.current_balance - amt
            print("withdrawn successfully")
            print("your current balnce is ", self.current_balance)
            


# In[17]:


obja = bank()
objb = bank()


# In[18]:


obja.update(1820642, 600, "john doe")


# In[19]:


obja.info()


# In[20]:


objb.info()


# In[21]:


obja.deposit(1000)


# In[22]:


obja.info()


# In[23]:


objb.withdraw(200)


# In[25]:


class bank:
    
    def __init__(self, i, o=0, n="shaktiman"):
        print("init gets called automatically")
        self.cid = i
        self.opening_balance = o
        self.name = n    
        self.current_balance = self.opening_balance
    
    def info(self):
        print("hello ", self.name)
        print("your current balance is ", self.current_balance)
        
    def deposit(self, amt):
        self.current_balance = self.current_balance + amt
        print("deposited successfully")
        
    def withdraw(self, amt):
        if self.current_balance < amt:
            print("insufficient balance")
        else:
            self.current_balance = self.current_balance - amt
            print("withdrawn successfully")
            print("your current balnce is ", self.current_balance)
            


# In[26]:


obja = bank(24580, 100)


# In[27]:


obja.info()


# In[29]:


objb = bank(25825)


# In[30]:


class bank:
    
    def __init__(self, i, o=0, n="shaktiman"):
        self.cid = i
        self.opening_balance = o
        self.name = n    
        self.current_balance = self.opening_balance
    
    def info(self):
        print("hello ", self.name)
        print("your current balance is ", self.current_balance)
        
    def deposit(self, amt):
        self.current_balance = self.current_balance + amt
        print("deposited successfully")
        
    def withdraw(self, amt):
        if self.current_balance < amt:
            print("insufficient balance")
            self.grade = 'D'
        else:
            self.current_balance = self.current_balance - amt
            print("withdrawn successfully")
            print("your current balnce is ", self.current_balance)
            


# In[31]:


obja = bank(24580, 100, "batman")
objb = bank(24700, 200, "ironman")


# In[32]:


obja.cid


# In[33]:


obja.withdraw(800)


# In[34]:


obja.grade


# In[35]:


objb.grade


# In[36]:


class A:
    dataa = 10
    datab = 20
    
    def display(self):
        print("dataa =", self.dataa)
        print("datab = ", self.datab)


# In[37]:


print(type(A))


# In[38]:


class A:
    dataa = 10
    datab = 20
    
    def display(self):
        print("dataa =", self.dataa)
        print("datab = ", self.datab)
        
    def funca():
        print("hi")


# In[39]:


objx = A()


# In[41]:


A.funca()         # A.funca()


# In[42]:


objx.funca()      # A.funca(objx)


# In[43]:


A.dataa


# In[44]:


A.dataa = 100


# In[45]:


objx.dataa


# In[46]:


objy = A()


# In[47]:


objy.dataa


# In[48]:


class A:
    dataa = 10
    datab = 20
    
    def display(self):
        print("dataa =", self.dataa)
        print("datab = ", self.datab)
        
    def funca():
        print("hi")


# In[49]:


A.funca()


# In[51]:


A.display()    #    -->   A.display()


# In[52]:


import sys


# In[53]:


sys.getsizeof(A)


# In[54]:


sys.getsizeof(obja)


# In[55]:


lista = [6, 8, 2, 4]
seta = {6, 8, 2, 4}


# In[56]:


print(sys.getsizeof(lista))
print(sys.getsizeof(seta)) 


# In[57]:


class A:
    dataa = 10
    _datab = 20
    __datac = 30
    __datad__ = 40
    
    def display(self):
        print("dataa =", self.dataa)
        print("_datab = ", self._datab)
        print("__datac = ", self.__datac)
        print("__datad__ = ", self.__datad__)
        
    def funca(self):
        print("hi")


# In[58]:


objx = A()
objy = A()


# In[59]:


print("dataa =", objx.dataa)
print("_datab = ", objx._datab)
print("__datac = ", objx.__datac)
print("__datad__ = ", objx.__datad__)


# In[60]:


print("__datad__ = ", objx.__datad__)


# In[61]:


objx.display()


# In[62]:


obja.__init__(444)


# In[68]:


class A:
    dataa = 10
    datab = 20
    
    def display(self):
        print("dataa =", self.dataa)
        print("_datab = ", self.datab)
        
    def update_1(self, val):
        self.dataa = val
        print("in 1")
    
    @classmethod
    def update_2(self, val):
        print("in 2")
        self.dataa = val
        
    def update_3():
        print("in 3")


# In[69]:


objx = A()


# In[70]:


objx.display()


# In[71]:


objx.update_1(100)


# In[72]:


objx.display()


# In[73]:


objx.update_2(200)


# In[74]:


objx.display()


# In[75]:


objy = A()


# In[76]:


objy = A()


# In[77]:


objy.display()


# In[88]:


class A:
    dataa = 10
    datab = 20
    
    def display(self):
        print("dataa =", self.dataa)
        print("_datab = ", self.datab)
        
    def update_1(self, val):
        self.dataa = val
        print("in 1")
    
    @classmethod
    def update_2(self, val):
        print("in 2")
        self.dataa = val
    
    @staticmethod
    def update_3(self):
        print("in 3") 


# In[90]:


objx = A()


# In[91]:


objx.update_3()      # A.update_3()


# In[92]:


objx.update_3("namaste")      # A.update_3()


# In[93]:


class A:
    dataa = 10
    datab = 20
    
    def display(self):
        print("dataa =", self.dataa)
        print("_datab = ", self.datab)


# In[94]:


objx = A()


# In[95]:


objx()


# In[96]:


print(objx)


# In[103]:


class A:
    dataa = 10
    datab = 20
    
    def display(self):
        print("dataa =", self.dataa)
        print("_datab = ", self.datab)
        
    def __call__(self):
        print("dataa =", self.dataa)
        print("datab = ", self.datab)
        
    def __repr__(self):
        return "hello"
    
    def __str__(self):
        return "hi"


# In[104]:


objx = A()


# In[105]:


objx()


# In[106]:


print(objx)


# In[107]:


import datetime


# In[108]:


n = datetime.datetime.now()


# In[109]:


print(n)


# In[110]:


n.__str__()


# In[111]:


n.__repr__()


# In[112]:


help(str)


# In[113]:


help(datetime.datetime)


# In[114]:


class unix:
    def cmd(self):
        print("great command line")
        
    def opensource(self):
        print("its opensource")
    
class linux(unix):
    def free(self):
        print("its free")


# In[115]:


obju = unix()
objl = linux()


# In[116]:


objl.opensource()


# In[118]:


class unix:
    def cmd(self):
        print("great command line")
        
    def opensource(self):
        print("its opensource")
    
class linux(unix):
    def free(self):
        print("its free")
        
class mobileOS():
    def port(self):
        print("quite portable in nature")
        
class android(linux, mobileOS):
    def ui(self):
        print("great ui") 


# In[119]:


obja = android()


# In[124]:


class unix:
    def cmd(self):
        print("great command line")
        
    def opensource(self):
        print("its opensource")
    
class linux(unix):
    def free(self):
        print("its free")
        
    def common(self):
        print("function from linux")
        
class mobileOS():
    def port(self):
        print("quite portable in nature")
        
    def common(self):
        print("function from mobileOS")
        
class android(linux, mobileOS):
    def ui(self):
        print("great ui") 


# In[125]:


obja = android()


# In[126]:


obja.common()


# In[127]:


class unix:
    def __init__(self):
        print("init of unix")
    
    def cmd(self):
        print("great command line")
        
    def opensource(self):
        print("its opensource")
    
class linux(unix):
    def free(self):
        print("its free")
        
    def common(self):
        print("function from linux")


# In[128]:


obju = unix()


# In[129]:


objl = linux()


# In[134]:


class unix:
    def __init__(self):
        print("init of unix")
    
    def cmd(self):
        print("great command line")
        
    def opensource(self):
        print("its opensource")
    
class linux(unix):
    def __init__(self):
        print("init of linux")
        
    def free(self):
        print("its free")
        
    def common(self):
        print("function from linux")


# In[135]:


objl = linux() 


# In[136]:


class unix:
    def __init__(self):
        print("init of unix")
    
    def cmd(self):
        print("great command line")
        
    def opensource(self):
        print("its opensource")
        
    def cmd(self):
        print("bash is cool")


# In[137]:


obju = unix()


# In[138]:


obju.cmd()


# In[139]:


from abc import ABC, abstractmethod


# In[146]:


class sample(ABC):
    
    @abstractmethod
    def funca(self):
        print("hey")
        pass
    


# In[147]:


obja = sample()


# In[145]:


obja.funca()


# In[148]:


class tample(sample):
    
    def funca(self):
        print("hey")
        pass


# In[149]:


objt = tample()


# In[150]:


class tample(sample):
    
    def funcb(self):
        print("hey")
        pass


# In[151]:


objt = tample()


# In[ ]:


morn = time(3, 50)
noon = time(1, 45)
even = time(2, 30)


# In[152]:


class time:
    def __init__(self, h, m):
        self.hours = h
        self.minutes = m
        
    def __str__(self):
        return f"{self.hours} hours and {self.minutes} minutes"


# In[153]:


morn = time(3, 50)
noon = time(1, 45)
even = time(2, 30)


# In[154]:


print(morn)


# In[155]:


total = morn + noon


# In[158]:


class time:
    def __init__(self, h=0, m=0):
        self.hours = h
        self.minutes = m
        
    def __str__(self):
        return f"{self.hours} hours and {self.minutes} minutes"
    
    def __add__(self, other):
        mina = self.hours*60 + self.minutes
        minb = other.hours*60 + other.minutes
        minc = mina + minb
        
        temp = time()
        
        temp.minutes = minc%60
        temp.hours = minc//60
        return temp


# In[159]:


3**2


# In[160]:


morn = time(3, 50)
noon = time(1, 45)
even = time(2, 30)


# In[161]:


total = morn + noon


# In[162]:


print(total)


# In[164]:


total = morn + noon + even

print(total)


# In[ ]:




