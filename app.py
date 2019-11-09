import math #needed for rounding up in median func
import numpy as np

data = [1, 3, 5, 2, 3, 7, 8, 4, 10, 3, 3, 0, 6, 7, 3, 0, 3, 0, 5, 7, 10, 1, 4, 9]
x_list = [3.3,4.4,5.5,6.71,6.93,4.168,9.779,6.182,7.59,2.167,7.042,10.791,5.313,7.997,5.654,9.27,3.1]
y_list = [1.7,2.76,2.09,3.19,1.694,1.573,3.366,2.596,2.53,1.221,2.827,3.465,1.65,2.904,2.42,2.94,1.3]

def mean(list): #get average
    return(float(sum(list)) / len(list))

def cov_matrix_calculation(data): # calculate covariance matrix of the data
    cov_matx = np.cov(data.T)
    return cov_matx

dataset = np.array([[1, 1, 1], [1, 2, 1], [1, 3, 2], [1, 4, 3]])
print(cov_matrix_calculation(dataset))

dataX = [1,2,3,4]
dataY = [1,1,2,3]
dataset2 = [[1, 1, 1], [1, 2, 1], [1, 3, 2], [1, 4, 3]]

def covariance(x,y):
    n = len(x)
    if n <= 0 or n != len(y):
        return
    xy = [((x[i]-mean(x))*(y[i]-mean(y))) for i in range(n)]
    return float(sum(xy))/float(n-1)


# print(covariance(dataX, dataY))


def covariance_final_attempt(dataset): #covariance function that takes a matrix and returns a covariance as a matrix
    average_of_column = [float(sum(l))/len(l) for l in zip(*dataset)] #[1.0, 2.5, 1.75] // zip(*dataset) = unzip // returns average of the columns in a 2D array 
    xyz_list = list(zip(*dataset)) #[(1, 1, 1, 1), (1, 2, 3, 4), (1, 1, 2, 3)]
    # print(average_of_column)
    # print(xyz_list)
    xy_list = [(1, 1), (2, 1), (3, 2), (4, 3)]
    summ = [sum(arr) for arr in zip(*xy_list)]
    print(summ)





covariance_final_attempt(dataset2)



















############################### PRACTICES ################################################
def practices(dataset):
    # for i in range(0, len(dataset)):
    #     print(i)
    # cov_matrix = (i*mean(dataset))
    average_of_column = [float(sum(l))/len(l) for l in zip(*dataset)] #[1.0, 2.5, 1.75] // zip(*dataset) = unzip // returns average of the columns in a 2D array 
    xyz_list = list(zip(*dataset)) #[(1, 1, 1, 1), (1, 2, 3, 4), (1, 1, 2, 3)]
    summ = [sum(arr) for arr in xyz_list] # [4, 10, 7]
    
    xy_list = [(1, 1), (2, 1), (3, 2), (4, 3)]
    summ = [sum(arr) for arr in xy_list] #[2, 3, 5, 7] //sum of rows 
    summ = [sum(arr) for arr in zip(*xy_list)] #10,7 #sum of columns

    # for l in list(zip(*dataset)):
        # print(l)
        # x.append(l)
    # final_results = [a+b for a, b in zip(dataset)]
    
    # print(x)
        
def median(list):
    length = len(list)
    sortedData = sorted(list)
    if length < 1: #if length < 0, return None
        return None
    if length % 2 == 1: #if list's length is odd
        return sortedData[length // 2]
    else: #if list's length is even, then get the average of the 2 middle
        firstElement = sortedData[length // 2]
        secondElement = sortedData[length // 2 - 1]
        return (firstElement + secondElement) / 2

def percentile(data, percent):
    if percent < 1.0:
        print("Plese input a percent from 1 - 100 only: ")
        return None
    sortedData = sorted(data)    
    index = (percent/100) * len(data)
    roundedUpIndex = math.ceil(index)
    return sortedData[roundedUpIndex-1]

def covariance_first_attempt(dataX, dataY):
    result = []
    length = len(dataX) - 1
    sortedX = sorted(dataX)
    sortedY = sorted(dataY)
    meanX = mean(dataX)
    meanY = mean(dataY)
    total = 0
    counter = 0
    while counter < 2:
        result.append([])
        if counter == 0:
            for i in range(len(dataX)): #cov(X,X)
                total += (sortedX[i] - meanX) * (sortedX[i] - meanX)
                if i == len(dataX)-1:
                    total /= length
                    result[counter].append(total)
            total = 0
            for i in range(len(dataX)): #cov(X,Y)
                total += (sortedX[i] - meanX) * (sortedY[i] - meanY)
                if i == len(dataX)-1:
                    total /= length
                    result[counter].append(total)
            total = 0
        elif counter == 1:
            for i in range(len(dataX)): #cov(Y,X)
                total += (sortedY[i] - meanY) * (sortedX[i] - meanX)
                if i == len(dataX)-1:
                    total /= length
                    result[counter].append(total)
            total = 0
            for i in range(len(dataX)): #cov(Y,Y)
                total += (sortedY[i] - meanY) * (sortedY[i] - meanY)
                if i == len(dataX)-1:
                    total /= length
                    result[counter].append(total)
            total = 0
        counter += 1
    # result [(i - meanX)*(j - meanY) for i, j in zip(sortedX,sortedY)]
    print(result)
    return result
