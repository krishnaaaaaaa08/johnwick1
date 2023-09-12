#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[15]:


df=pd.read_csv('TCS.NS.csv',index_col=0,parse_dates=True)


# In[16]:


df.head()


# In[17]:


df.tail()


# In[18]:


len(df)


# In[19]:


df.dropna(axis=0,inplace=True)


# In[20]:


df['bnh_returns_log_ret']=np.log(df['Adj Close']/df['Adj Close'].shift(1))


# In[21]:


df["indicator"]=np.where(df['bnh_returns_log_ret']>0,"positive",0)
df["indicator"]=np.where(df['bnh_returns_log_ret']<0,"negative",df["indicator"])


# In[22]:


df.head()


# In[24]:


df["indicator"].value_counts()


# In[25]:


import numpy as np


# In[26]:


np.random.seed(1234)


# In[27]:


numbers=np.random.uniform(0,1,24)


# In[28]:


numbers


# In[29]:


print(numbers)


# In[30]:


len(numbers)


# In[31]:


np.min(numbers)


# In[32]:


np.max(numbers)


# In[33]:


numbers[20:24]


# In[35]:


plt.figure(figsize=(10,6))
plt.hist(df['bnh_returns_log_ret'])
plt.title('HISTOGRAM OF LOG RETURNS')
plt.ylabel('frequency')
plt.xlabel('bnh_returns_log_ret')
plt.show()


# In[42]:


plt.figure(figsize=(16,10))
plt.scatter(df['Open'],df['Close'])
plt.title('scatter plot of the log returns')
plt.ylabel('Close')
plt.xlabel('Open')
plt.show()


# In[48]:


df['20_day_sma']=df['Adj Close'].rolling(window=20,center=False).mean()


# In[46]:


df['20_day_sma']=df['Adj Close'].rolling(window=20,center=False).mean() #rolling moving average of the adj close 20 days


# In[49]:


df['20_day_std']=df['Adj Close'].rolling(window=20,center=False).std()


# In[50]:


df.tail()


# In[ ]:




