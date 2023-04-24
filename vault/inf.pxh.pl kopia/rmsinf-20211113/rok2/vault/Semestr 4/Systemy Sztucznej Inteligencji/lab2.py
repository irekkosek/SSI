import numpy as np
import random
import pandas as pd
import seaborn as snd #charts
import random
snd.set_palette('husl') #color palette

iris = pd.read_csv("iris.csv")


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


class KNN:
    @staticmethod
    def minkowski(vec1, vec2, m):
        distance = 0
        for i in range(len(vec2) - 1):
            distance += abs(vec2[i] - vec1[i]) ** m
        distance = float(distance ** (1 / m))
        return distance


    @staticmethod
    def sorting(trainList, distances):
        trainBase = trainList.copy()
        for i in range(len(trainBase)):
            ready = True
            print(".", end="")
            for j in range(len(trainBase)-i-1):
                if distances[j]>distances[j+1]:
                    distances[j], distances[j+1] = distances[j+1], distances[j]
                    trainBase.iloc[j], trainBase.iloc[j+1] = trainBase.iloc[j+1], trainBase.iloc[j]
                    ready = False
            if ready:
                break
        return distances, trainBase


    @staticmethod
    def clustering(valBase, trainBase, k, m):  # m = 2 -> euklides
        corrected = 0
        n = len(valBase)
        fail = {"Setosa": 0, "Virginica": 0, "Versicolor": 0}
        types = {"Setosa": 0, "Virginica": 0, "Versicolor": 0}
        for irisNumber in range(n):
            testSample = valBase.iloc[irisNumber]
            realIris = valBase.iloc[irisNumber].variety
            types[realIris] += 1
            classes = {"Setosa": 0, "Virginica": 0, "Versicolor": 0}
            print("\n({}/{})".format(irisNumber+1, n))
            # obliczyć odległości
            distances = []
            for i in range(len(trainBase)):
                distances.append(KNN.minkowski(testSample, trainBase.iloc[i], m))
            # posortować klasy wg odległości
            distances, trainBase = KNN.sorting(trainBase, distances)
            # głosowanie
            for i in range(0, k, 1):
                classes[trainBase.iloc[i].variety] += 1
            # zwróć przewidywaną klasę
            aiIris = max(classes,key=classes.get)
            if aiIris == realIris:
                corrected += 1
            else:
                fail[realIris] += 1
        # wypisz staty
        print("\n\tSTATYSTYKI:\n"
              "k = {}\nm = {}".format(k, m))
        k = 0
        for key, value in types.items():
            all = list(types.values())[k]
            this = list(fail.values())[k]
            diff = all-this
            print("{} - {}/{} - {:.2f}%".format(key, diff, all, diff/all*100))
            k+=1
        accuracy = corrected/len(valBase)*100
        print("Dokładność - {:.2f}%".format(accuracy))
        return accuracy



#irisNormalized = DataProcessing.normalize(irisShuffled)
#irisNormalizedSplitted = DataProcessing.splitSet(irisNormalized)
#irisSplitted[0].head()

acc = []
for k in range(2, 6, 1):
    irisShuffled = DataProcessing.shuffle(iris)
    irisTrain, irisVal = DataProcessing.splitSet(irisShuffled)
    acc.append(KNN.clustering(irisVal, irisTrain, k, 2))
for k in range(2, 6, 1):
    print("Dla k = {} uzyskano {:.2f}% dokładności.".format(k, acc[k-2]))

