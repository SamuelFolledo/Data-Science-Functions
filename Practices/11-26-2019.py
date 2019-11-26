import random
import numpy as np

a = [1,2,3]
b = [10,15,20]

################################################################################
#  1) add each element in a list a[i]+b[i] and return as a list
def add_lists(a,b): #1) My answer
    length = len(a)
    result=[]
    for index in range(length):
        result.append(a[index] + b[index])
    return result
# print(add_lists(a,b))

def add_lists2(x,y): #1) Milad's answer
    z = [i+j for i,j in zip(x,y)] #array manipulation using list comprehension
    return z
# print(add_lists2(a,b))

################################################################################
# 2) Get maximum element from a list
def max_element(arr): #2) My answer
    maxNum = 0
    for num in arr:
        if num > maxNum:
            maxNum = num
    return maxNum
# print(max_element(b))

def max_element2(x): #2) Milad's answer
    max_element = x[0]
    for num in x[1:]: #all elements from the list starting from index 1
        if num > max_element:
            max_element = num
    return max_element
# print(max_element2(b))

################################################################################
# 3) for two lists, return sum of a[i]*b[i]
# Hint: covariance = xy = [((x[i]-mean(x))*(y[i]-mean(y))) for i in range(n)]
def sum_multiplied_list(a,b): #my solution
    return sum([(a[i]*b[i]) for i in range(len(a))])
# print(sum_multiplied_list(a,b))

################################################################################
# 4) for list a, return sum of (a[i] - mean(a))^2
def answer(a): #my answer
    return sum([(a[i]-np.mean(a))**2 for i in range(len(a))])
# print(answer(a))
# print(answer(b))

################################################################################
# 5) for list a, given scalar w1 and w0, return a list yPred[i] = w1*a[i] + w0
def get_y_pred(a, w1, w0): #my solution
    return [(w1*num+w0) for num in a]
print(get_y_pred(a,0.5,1))



################################################################################