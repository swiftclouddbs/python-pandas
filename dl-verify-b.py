#!/usr/bin/env python
# coding: utf-8

# In[17]:


import sys
import pandas as pd
import numpy as np


# In[18]:


licenses = pd.read_csv('/home/dba/python_dev/md-dlicense/dl-test-data.csv')
#print(licenses[['LastName', 'DLNum']])


# In[19]:


licenses.DLNum= licenses.DLNum.str.replace('-','')


# In[ ]:





# In[20]:


licenses['NoDash'] = licenses['DLNum'].str[:4]
#licenses[['LastName','NoDash']]


# In[21]:


licenses['NewLast'] = licenses['LastName'].str.replace("[AEIOUWYH]","")


# In[22]:




# In[23]:


licenses['FirstC'] = licenses['NewLast'].str[0]
licenses['SecC'] = licenses['NewLast'].str[1]
licenses['ThirdC'] = licenses['NewLast'].str[2]
licenses['FourthC'] = licenses['NewLast'].str[3]
licenses['FourthC'] = licenses['FourthC'].fillna(0)


# In[24]:


licenses['SecC'] = licenses['SecC'].replace(['A','E','I','O','U','W','Y','H'],'')
licenses['SecC'] = licenses['SecC'].replace(['B','P','F','V'],'1')
licenses['SecC'] = licenses['SecC'].replace(['C','S','K','G','J','Q','X','Z'],'2')
licenses['SecC'] = licenses['SecC'].replace(['D','T'],'3')
licenses['SecC'] = licenses['SecC'].replace(['L'],'4')
licenses['SecC'] = licenses['SecC'].replace(['M','N'],'5')
licenses['SecC'] = licenses['SecC'].replace(['R'],'6')
licenses['ThirdC'] = licenses['ThirdC'].replace(['A','E','I','O','U','W','Y','H'],'')
licenses['ThirdC'] = licenses['ThirdC'].replace(['B','P','F','V'],'1')
licenses['ThirdC'] = licenses['ThirdC'].replace(['C','S','K','G','J','Q','X','Z'],'2')
licenses['ThirdC'] = licenses['ThirdC'].replace(['D','T'],'3')
licenses['ThirdC'] = licenses['ThirdC'].replace(['L'],'4')
licenses['ThirdC'] = licenses['ThirdC'].replace(['M','N'],'5')
licenses['ThirdC'] = licenses['ThirdC'].replace(['R'],'6')
licenses['FourthC'] = licenses['FourthC'].replace(['A','E','I','O','U','W','Y','H'],'')
licenses['FourthC'] = licenses['FourthC'].replace(['B','P','F','V'],'1')
licenses['FourthC'] = licenses['FourthC'].replace(['C','S','K','G','J','Q','X','Z'],'2')
licenses['FourthC'] = licenses['FourthC'].replace(['D','T'],'3')
licenses['FourthC'] = licenses['FourthC'].replace(['L'],'4')
licenses['FourthC'] = licenses['FourthC'].replace(['M','N'],'5')
licenses['FourthC'] = licenses['FourthC'].replace(['R'],'6')
licenses


# In[25]:


licenses.FourthC = licenses.FourthC.astype(str)
licenses['Coded'] = licenses[['FirstC', 'SecC', 'ThirdC', 'FourthC']].agg(''.join, axis=1)


# In[26]:


#print(licenses)


# In[27]:


#comparison_column = np.where(df["col1"] == df["col2"], True, False)
#df["equal"] = comparison_column
same = np.where(licenses["NoDash"] == licenses["Coded"], True, False)
licenses["same_key"] = same


# In[28]:


print(licenses.same_key)


# In[ ]:




