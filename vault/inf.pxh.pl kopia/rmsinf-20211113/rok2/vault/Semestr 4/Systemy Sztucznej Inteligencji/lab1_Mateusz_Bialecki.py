#!/usr/bin/env python
# coding: utf-8

# In[76]:


import numpy as np
import pandas as pd #CSV files
import matplotlib.pyplot as plt
import random
import seaborn as sns
sns.set_palette('husl')


# In[77]:


iris = pd.read_csv('iris.csv')


# In[78]:


iris.head()


# In[87]:


g1=sns.violinplot(y="variety",x="sepal.length",data=iris, inner='quartile')
g2=sns.violinplot(y="variety",x="sepal.width",data=iris, inner='quartile')
g3=sns.violinplot(y="variety",x="petal.length",data=iris, inner='quartile')
g4=sns.violinplot(y="variety",x="petal.width",data=iris, inner='quartile')


# In[79]:


class DataProcessing:
    @staticmethod
    def shuffle(X):
        for i in range(len(X)-1,0,-1):
            j = random.randint(0, i)
            X.iloc[i], X.iloc[j] = X.iloc[j], X.iloc[i]
        return X
    #normalizacja
    #x = x-min/max-min
    # dla każdej kolumny znajdujemy min/max; następnie w danej kolumnie przeliczamy wartosc zgodnie z powyższą formułą
    @staticmethod
    def normalize(X):
        #TODO
        result = X.drop("variety", axis=1)
        result = (result-result.min())/(result.max()-result.min())
        result = result.join(X["variety"])
        return result
    
    #podział zbioru
    @staticmethod
    def splitSet(X):
        split = int(len(X)*0.7)
        training_set = X[:split] 
        validation_set =X[split:]
        return [training_set, validation_set]


# In[80]:


iris_shuffled = DataProcessing.shuffle(iris)


# In[81]:


training_set, validation_set = DataProcessing.splitSet(iris_shuffled)


# In[82]:


iris_shuffled


# In[83]:


iris_normalized = DataProcessing.normalize(iris_shuffled)


# In[84]:


iris_normalized


# In[ ]:




