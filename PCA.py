#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


a = np.array([[1,2,3,4],[2,4,6,8],[3,6,9,12],[4,8,12,16]])
a


# In[3]:


b = np.array([1,2,3,4])


# In[4]:


c = b - b.mean()
c


# In[5]:


aa = a-np.mean(a)
np.matmul(aa,aa.T)


# In[6]:


np.dot(aa,aa.T)


# In[7]:


aa.dot(aa)


# In[8]:


np.cov(a)


# In[9]:


b = pd.DataFrame(np.array([[2.1,8],[2.5,10],[3.6,12],[4,14]]), columns=['num1','num2'])
b.cov()


# In[10]:


bb = np.array([[2.1,8],[2.5,10],[3.6,12],[4,14]])
np.cov(bb)


# In[12]:


cc = np.array([[90,90,60,60,30],[60,90,60,60,30],[90,30,60,90,30]])
cc


# In[13]:


np.cov(cc)

