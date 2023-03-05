#!/usr/bin/env python
# coding: utf-8

# # Important Jupyter shortcut
# tab to give function methods
# shift&tab parameter and help
# command&/ to comment ⌘/: comment

# # Cardio Good Fitness Case Study - Descriptive Statistics
# The market research team at AdRight is assigned the task to identify the profile of the typical customer for each treadmill product offered by CardioGood Fitness. The market research team decides to investigate whether there are differences across the product lines with respect to customer characteristics. The team decides to collect data on individuals who purchased a treadmill at a CardioGoodFitness retail store during the prior three months. The data are stored in the CardioGoodFitness.csv file.
# 
# ### The team identifies the following customer variables to study: 
#   - product purchased, TM195, TM498, or TM798; 
#   - gender; 
#   - age, in years; 
#   - education, in years; 
#   - relationship status, single or partnered; 
#   - annual household income ; 
#   - average number of times the customer plans to use the treadmill each week; 
#   - average number of miles the customer expects to walk/run each week; 
#   - and self-rated fitness on an 1-to-5 scale, where 1 is poor shape and 5 is excellent shape.
# 
# ### Perform descriptive analytics to create a customer profile for each CardioGood Fitness treadmill product line.

# In[43]:


# # Load the necessary packages
# import numpy as np
# import pandas as pd
# # import numpy as np
# # import pandas as pd
import pandas as pd
import numpy as np


# In[44]:


mydata = pd.read_csv('r.csv')


# In[45]:


mydata.head(5)


# In[46]:


mydata.columns


# In[47]:


mydata.rename(columns={"Unnamed": "Age", "Unnamed": "Gender"}, inplace=True)


# In[48]:


mydata.columns


# In[49]:


mydata_cols


# In[50]:


mydata.columns=mydata_cols


# In[51]:


mydata.head()


# #### Load the Cardio Dataset
# mydata = pd.read_csv('r.csv')
# # /Users/nooruldeen/Dropbox/Teaching/Statistics/٠Practical/Lectures/2/CardioGoodFitness.csv
# # mydata = pd.read_csv('CardioGoodFitness.csv')

# In[39]:


# mydata.head()
# mydata.columns
mydata.info()


# In[40]:


mydata.describe()


# In[41]:


mydata.info()


# In[42]:


#+ import matplotlib.pyplot as plt
imprt matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

mydata.hist(figsize=(30,40))

plt.show()


# In[10]:


mydata.hist(['Age'], figsize=(30,40))
plt.show()


# In[11]:


import seaborn as sns

sns.boxplot(x="Gender", y="Age", data=mydata)
# sns.boxplot(x="Gender", orient= "h", data=mydata)


# In[12]:


pd.crosstab(mydata['No.of.people'],mydata['Gender'] )


# In[13]:


pd.crosstab(mydata['Product'],mydata['City'] )


# In[14]:


sns.countplot(x="Product", hue="Gender", data=mydata)


# In[15]:


pd.pivot_table(mydata, index=['Product', 'Gender'],
                     columns=[ 'MaritalStatus'], aggfunc=len)


# In[16]:


pd.pivot_table(mydata,'Income', index=['Product', 'Gender'],
                     columns=[ 'MaritalStatus'])


# In[17]:


pd.pivot_table(mydata,'Miles', index=['Product', 'Gender'],
                     columns=[ 'MaritalStatus'])


# In[18]:


sns.pairplot(mydata)


# In[19]:


mydata['Age'].std()


# In[ ]:


mydata['Age'].mean()


# In[ ]:


sns.distplot(mydata['Age'])


# In[20]:


mydata.hist(by='Gender',column = 'Age')


# In[21]:


mydata.hist(by='Gender',column = 'Income')


# In[22]:


mydata.hist(by='Gender',column = 'Miles')


# In[23]:


mydata.hist(by='Product',column = 'Miles', figsize=(20,30))


# In[24]:


corr = mydata.corr()
corr


# In[25]:


sns.heatmap(corr, annot=True)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




