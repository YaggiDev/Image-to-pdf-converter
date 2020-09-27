#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
from fpdf import FPDF


# In[2]:


i = 0
file_list = []
for root, dir, files in os.walk("."):
    for filename in files:
        print(i,") ",filename)
        file_list.append(str(filename))
        i+=1


# In[ ]:


indexes = input("Which files u want to add (ex.:  1,2,3): ")


# In[11]:


name = input("Name of the output file (ex.: filename) : ")
name = name + ".pdf"


# In[6]:


indexes = indexes.split(',')


# In[7]:


i = 0
indexes_ = []
while i < len(indexes):
    print(i)
    indexes_.append(int(indexes[i]))
    i = i +1
indexes_


# In[8]:


imgs = []
for ind in indexes_:
    imgs.append(file_list[ind])
imgs


# In[10]:


pdf = FPDF()
try:
    for image in imgs:
        pdf.add_page()
        pdf.image(image)
except:
    print("Upsss. Something went wrong. Check if the indexes were given correctly or the filename is proper.")
pdf.output(name, "F")


# In[ ]:




