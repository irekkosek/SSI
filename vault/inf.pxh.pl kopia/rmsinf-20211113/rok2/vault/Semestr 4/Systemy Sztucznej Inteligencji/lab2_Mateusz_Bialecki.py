#!/usr/bin/env python
# coding: utf-8

# In[115]:


import numpy as np
import pandas as pd #CSV files
import matplotlib.pyplot as plt
import random
import seaborn as sns
sns.set_palette('husl')


# In[116]:


iris = pd.read_csv('iris.csv')


# In[117]:


iris.head()


# In[118]:


g1=sns.violinplot(y="variety",x="sepal.length",data=iris, inner='quartile')
g2=sns.violinplot(y="variety",x="sepal.width",data=iris, inner='quartile')
g3=sns.violinplot(y="variety",x="petal.length",data=iris, inner='quartile')
g4=sns.violinplot(y="variety",x="petal.width",data=iris, inner='quartile')


# In[119]:


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


# In[120]:


iris_shuffled = DataProcessing.shuffle(iris)


# In[121]:


training_set, validation_set = DataProcessing.splitSet(iris_shuffled)


# In[ ]:





# In[122]:


iris_normalized = DataProcessing.normalize(iris_shuffled)


# In[ ]:





# In[123]:


class KNN:
    @staticmethod
    def minkowskiMetric(v1, v2, m):

        distance = 0
        for i in range(len(v1)-1):
            distance += abs(v1.iloc[i]**m - v2.iloc[i]**m)
        distance = distance**(1/m)
        return distance
    
    def clustering(sample, X, k):
        distances = []
        classes = {'Setosa': 0, 'Virginica': 0, 'Versicolor': 0}
        for i in X.index:
            distances.append([KNN.minkowskiMetric(sample, X.iloc[i], 2), X.iloc[i].variety])
            
        distances = sorted(distances)                    
        
        #glosowanie
        for i in range(k):
            classes[distances[i][1]]+=1

        return max(classes, key=classes.get)


# In[127]:


#testowanie

k=3
correct = 0

for sample in validation_set.iloc:
    
    AI_answear = KNN.clustering(sample, training_set, k)

    if AI_answear == sample.variety:
        correct += 1
    
accuracy = correct/len(validation_set)*100
print("accuracy: ", accuracy, "correct: ", correct)


# In[ ]:





# In[ ]:




