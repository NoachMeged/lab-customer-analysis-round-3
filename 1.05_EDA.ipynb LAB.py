#!/usr/bin/env python
# coding: utf-8

# In[54]:


#  Install and read.csv
get_ipython().system('pip install matplotlib')
get_ipython().system('pip install seaborn')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

data = pd.read_csv('/Users/noachmeged/Documents/Ironhack/Labs/lab-customer-analysis-round-3/files_for_lab/csv_files/marketing_customer_analysis.csv')


# In[66]:


#  Show DataFrame info
data.info()


# In[18]:


# Describe the dateframe
summary = data.describe().T
summary


# In[51]:


# Show a plot of the total number of responses.
plt.figure(figsize=(5,8))
sns.countplot(x="Response", data=data)


# In[61]:


# Show a plot of the response rate by the sales channel.
data["Sales Channel"].value_counts()
plt.figure(figsize=(5,8))
sns.countplot(x="Response",hue= "Sales Channel",  data=data)


# In[64]:


# Show a plot of the response rate by the total claim amount.
plt.figure(figsize=(5,3))

sns.barplot(x="Response", y="Total Claim Amount", data=data)
plt.show()


# In[69]:


# Show a plot of the response rate by income.
plt.figure(figsize=(5,3))

sns.barplot(x="Response", y="Income", data=data)
plt.show()


# In[71]:


# Show a plot of the response rate by income.
sns.boxplot(x="Response", y="Income", data=data) # same as sns.boxplot(data["median_home_val"])
plt.show()

