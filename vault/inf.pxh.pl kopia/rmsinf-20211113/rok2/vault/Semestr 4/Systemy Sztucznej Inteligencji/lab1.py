#!/usr/bin/env python
# coding: utf-8

# In[49]:


import numpy as np
import random
import pandas as pd
import seaborn as snd #charts
snd.set_palette('husl') #color palette


# In[50]:


iris = pd.read_csv("iris.csv")


# In[51]:


iris.head()


# In[52]:


iris.describe()


# In[53]:


iris.info()


# In[54]:


snd.pairplot(iris, hue="variety", markers="+")


# In[55]:


g1=snd.violinplot(y="variety",x="sepal.length",data=iris, inner='quartile')
g2=snd.violinplot(y="variety",x="sepal.width",data=iris, inner='quartile')
g3=snd.violinplot(y="variety",x="petal.length",data=iris, inner='quartile')
g4=snd.violinplot(y="variety",x="petal.width",data=iris, inner='quartile')


# In[56]:


#potasowanie, normalizacja, podzieli na 2 podzbiory
class DataProcessing:
    @staticmethod
    def shuffle(X):
        for i in range(len(X)-1, 0, -1):
            j = random.randint(0,i)
            X.iloc[i], X.iloc[j] = X.iloc[j], X.iloc[i]
        return X

    @staticmethod
    def splitSet(X):
        split = int(len(X)*0.7)
        XTrain = X.iloc[:split, :]
        XVal = X.iloc[split:, :]
        return XTrain, XVal

    @staticmethod
    def normalize(Y):
        X = Y.copy()
        #normalizuje zbiór X
        # w każdej kolumnie znaleźć min i max
        #<4.3; 7.9> -> <0; 1>
        #min = 4.3 => 0
        #max = 7.9 => 1
        #x = (x-min)/(max-min) # x - aktualna wartość
        values = X.select_dtypes(exclude="object") # no variety column
        columnNames = values.columns.tolist()
        for column in columnNames:
            data = X.loc[:, column]
            maximum = max(data)
            minimum = min(data)
            substractionMaxMin = maximum - minimum
            for row in range(0,len(X),1):
                value = (X.at[row, column] - minimum) / substractionMaxMin
                X.at[row, column] = value
        return X


# In[57]:


irisShuffled = DataProcessing.shuffle(iris)
irisNormalized = DataProcessing.normalize(irisShuffled)
irisSplitted = DataProcessing.splitSet(irisShuffled)
irisNormalizedSplitted = DataProcessing.splitSet(irisNormalized)
irisSplitted[0].head()


# In[58]:


irisNormalizedSplitted[0].head()


# In[59]:


irisSplitted[1].head()


# In[60]:


irisNormalizedSplitted[1].head()


# In[ ]:




