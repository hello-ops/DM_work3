#!/usr/bin/env python
# coding: utf-8

# In[1]:


import datetime as dt
import pandas as pd


# In[24]:


data = pd.read_csv('hotel_data/hotel_bookings.csv')


# In[25]:


columns_name =[column for column in data]
print(columns_name)


# In[26]:


data['arrival_date_month']


# In[28]:


data['arrival_date_month'] = pd.to_datetime(data['arrival_date_month'], format='%B').dt.month
print(data['arrival_date_month'])


# In[29]:


a = {"year":data["arrival_date_year"].values,"month":data["arrival_date_month"].values,"day":data["arrival_date_day_of_month"].values}
print(a)
pd.to_datetime(a)


# In[31]:


data['reservation_status_date'].map(dt.datetime.toordinal)


# In[2]:


a = pd.DataFrame()
a['x'] = [1, 2, 3]
a['y'] = ['a', 'b', pd.NaT]


# In[3]:


print(a)


# In[10]:


a = a.drop(a[a['y'].isna()].index)
a


# In[ ]:




