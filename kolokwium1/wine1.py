# In[1]:

import numpy as np
import random as rd
import seaborn as sns
import math
import pandas as pd #przetwarzanie danych
import statistics

# In[2]:

redWine = pd.read_csv(r'winequality-red.csv', sep=',')
whiteWine = pd.read_csv(r'winequality-white.csv', sep=";")

# %%

redWine.head()

# %%

redWine.iloc[0][0]

# %%

list(redWine.columns)

# %%

class ProcessingData:
    @staticmethod
    def ShuffleData(df: pd.DataFrame):
        for i in range(len(df)):
            rand_i=rd.randint(0,len(df)-1)
            df.loc[i],df.loc[rand_i] = df.loc[rand_i],df.loc[i]
        return df
    @staticmethod
    def SplitData(df:pd.DataFrame,x:int,y:int):
        if x+y>100:
            print("Podano zbyt dużą ilość danych do podziału")
            return
        train_set,test_set = pd.DataFrame(),pd.DataFrame()
        for i in range(len(df)):
            if rd.random()<x/100:
                train_set = train_set.append(df.loc[i])
            else:
                test_set = test_set.append(df.loc[i])
        return train_set,test_set
    @staticmethod
    def NormalizeData(df:pd.DataFrame):
        for atributte in df.columns[:-1]:
            mean = df[atributte].mean()
            stddev = df[atributte].std()
            df[atributte] = (df[atributte]-mean)/stddev
        return df
# %%

wineDF = ProcessingData.ShuffleData(redWine)
train_set,test_set = ProcessingData.SplitData(wineDF,70,30)
train_set = ProcessingData.NormalizeData(train_set)

# %%

train_set
# %%

class KNN:
    @staticmethod
    def distance(x: pd.Series, y:pd.Series, m:int) -> float:
        return sum([abs(x-y)**m for x,y in zip(x,y)])**(1/m)
    @staticmethod
    def get_neighbours(df:pd.DataFrame,x:pd.Series,k:int,m:int) -> list:
        distances = []
        for i in range(len(df)):
            distances.append((KNN.distance(x,df.iloc[i],m),df.iloc[i]))
        distances.sort(key=lambda x:x[0])
        return distances[:k]
    @staticmethod
    def get_class(neighbours:list) -> int:
        classes = {}
        for i in range(len(neighbours)):
            if neighbours[i][1][-1] not in classes:
                classes[neighbours[i][1][-1]] = 1
            else:
                classes[neighbours[i][1][-1]] += 1
        return max(classes,key=classes.get)
    @staticmethod
    def get_accuracy(df:pd.DataFrame,test_set:pd.DataFrame,m:int) -> float:
        correct = 0
        for i in range(len(test_set)):
            neighbours = KNN.get_neighbours(df,test_set.iloc[i],5,m)
            if KNN.get_class(neighbours) == test_set.iloc[i][-1]:
                correct += 1
        print("Good predicted: ",correct)
        print("Bad predicted: ",len(test_set)-correct)
        return f"{round((correct/len(test_set))*100,2)}%"
    # man

# %%

wineDF = ProcessingData.ShuffleData(redWine)
wineDF = ProcessingData.NormalizeData(wineDF)
train_set,test_set = ProcessingData.SplitData(wineDF,70,20)
   
# %%

print(KNN.get_accuracy(train_set,test_set,2))

# %%

class softClassificator:
    @staticmethod
    def fit(df: pd.DataFrame):
        means = {}
        mins = {}
        maxes = {}
        for Class in df.iloc[:,-1].unique():
            means[Class] = {}
            mins[Class] = {}
            maxes[Class] = {}
            for atributte in df.columns:
                if atributte != df.columns[-1]:
                    means[Class][atributte] = df[df.iloc[:,-1] == Class][atributte].mean()
                    mins[Class][atributte] = df[df.iloc[:,-1] == Class][atributte].min()
                    maxes[Class][atributte] = df[df.iloc[:,-1] == Class][atributte].max()
                    for row in df.index:
                        if df.loc[row,atributte] < means[Class][atributte]:
                            df.loc[row,atributte] = 0
                        else:
                            df.loc[row,atributte] = 1
        return df,means,mins,maxes

    @staticmethod
    def predict_sample(sample:pd.Series, means:dict, mins:dict, maxes:dict) -> str:
        for Class in means.keys():
            for atributte in means[Class].keys():
                if sample[atributte] < means[Class][atributte]:
                    sample[atributte] = 0
                else:
                    sample[atributte] = 1
        max_probability = 0
        max_Class = ""
        for Class in means.keys():
            probability = 1
            for atributte in means[Class].keys():
                if sample[atributte] == 0:
                    probability *= (1-means[Class][atributte])
                else:
                    probability *= means[Class][atributte]
            if probability > max_probability:
                max_probability = probability
                max_Class = Class
        return max_Class

    @staticmethod
    def accuracy(df: pd.DataFrame, means:dict, mins:dict, maxes:dict) -> float:
        correct = 0
        for row in df.index:
            if df.loc[row,df.columns[-1]] == softClassificator.predict_sample(df.loc[row],means,mins,maxes):
                correct += 1
        return f"{round(correct/len(df) * 100,2)}%"
    # man

# %%

class softClassificator:
    @staticmethod
    def fit(df: pd.DataFrame):
        means = {}
        mins = {}
        maxes = {}
        for Class in df.iloc[:,-1].unique():
            means[Class] = {}
            mins[Class] = {}
            maxes[Class] = {}
            for atributte in df.columns:
                if atributte != df.columns[-1]:
                    means[Class][atributte] = df[df.iloc[:,-1] == Class][atributte].mean()
                    mins[Class][atributte] = df[df.iloc[:,-1] == Class][atributte].min()
                    maxes[Class][atributte] = df[df.iloc[:,-1] == Class][atributte].max()
                    for row in df.index:
                        if df.loc[row,atributte] < means[Class][atributte]:
                            df.loc[row,atributte] = 0
                        else:
                            df.loc[row,atributte] = 1
        return df,means,mins,maxes

    @staticmethod
    def predict_sample(sample:pd.Series, means:dict, mins:dict, maxes:dict) -> str:
        for Class in means.keys():
            for atributte in means[Class].keys():
                if sample[atributte] < means[Class][atributte]:
                    sample[atributte] = 0
                else:
                    sample[atributte] = 1
        max_probability = 0
        max_Class = ""
        for Class in means.keys():
            probability = 1
            for atributte in means[Class].keys():
                if sample[atributte] == 0:
                    probability *= (1-means[Class][atributte])
                else:
                    probability *= means[Class][atributte]
            if probability > max_probability:
                max_probability = probability
                max_Class = Class
        return max_Class

    @staticmethod
    def accuracy(df: pd.DataFrame, means:dict, mins:dict, maxes:dict) -> float:
        correct = 0
        for row in df.index:
            if df.loc[row,df.columns[-1]] == softClassificator.predict_sample(df.loc[row],means,mins,maxes):
                correct += 1
        return f"{round(correct/len(df) * 100,2)}%"
# %%

wineDF = ProcessingData.NormalizeData(redWine)
wineDF = ProcessingData.ShuffleData(wineDF)
train_set,test_set = ProcessingData.SplitData(wineDF,70,30)

# %%

for i in range(4):
    wineDF = ProcessingData.ShuffleData(wineDF)
    train_set,test_set = ProcessingData.SplitData(wineDF,70,30)
    train_set,means,mins,maxes = softClassificator.fit(train_set)
    print(softClassificator.accuracy(test_set,means,mins,maxes))
    
# %%
