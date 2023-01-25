#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[8]:


from bs4 import BeautifulSoup
import requests


# In[9]:


print("hi")


# In[64]:


j=requests.get("https://www.glassdoor.ca/Salaries/software-engineer-salary-SRCH_KO0,17_IP2.htm")


# In[65]:


print(j)


# In[68]:


webpage=j.text


# In[69]:


soup=BeautifulSoup(webpage,'lxml')


# In[70]:


soup.find_all('h3')[0].text


# In[63]:


names=[]
h_3= soup.find_all('a',class_="css-f3vw95 e1aj7ssy3")
for i in h_3:
    print(i.text)
    names.append(i.text)
    
    
print(names)


# In[71]:


h_3= soup.find_all('a',class_="css-f3vw95 e1aj7ssy3")
for i in h_3:
    print(i.text)
    names.append(i.text)
    
    
print(names)


# In[ ]:





# In[ ]:





# In[ ]:





# In[50]:


for i in h_3:
    j=i.find('a',class_="css-f3vw95 e1aj7ssy3")
    
    print(j)


# In[ ]:


h

