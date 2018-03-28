import pandas as pd
import numpy as np

def mean(values):
	return sum(values) / float(len(values))

def covariance(x, x_mean, y, y_mean):
    covar = 0.0
    for i in range(len(x)):
        covar += (x[i] - x_mean) * (y[i] - y_mean)
    return covar

def variance(values, mean):
    return sum([(x-mean)**2 for x in values])

def training(data, target):
    B = []
    y = target
    y_mean = mean(y)
    #print(len(data.columns))
    for column in data:
        x = data[column]
        x_mean = mean(data[column])
        B.append((covariance(x, x_mean, y, y_mean) / variance(x, x_mean)))
        #print("mean = ", mean(data[column]))
        #print(data[column])
        #print(column)
    return B


data = pd.read_csv('train.csv')
Y = data['shares']
data = data.drop(['url', 'shares'], axis=1)


for i in data:
    predictions = np.array(data[i])
    targets = np.array(Y)
    V = np.sqrt(((predictions - targets) ** 2).mean())
    print(V)

#coefficients = training(data, Y)

#print(coefficients)

#for row in range(0,len(data)):
#    X = data.ix[row][1:-2]
#    Y = data.ix[row][-1]
##    for col in X:
#        print(col)
#   
#    if row == 0:
#        break        
