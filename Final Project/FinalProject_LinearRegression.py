import random
import numpy as np
import matplotlib.pyplot as plt

# Running Distance in Mile
x = np.array([3.3,4.4,5.5,6.71,6.93,4.168,9.779,6.182,7.59,2.167,
                         7.042,10.791,5.313,7.997,5.654,9.27,3.1])

# Water Drinks in Litre
y = np.array([1.7,2.76,2.09,3.19,1.694,1.573,3.366,2.596,2.53,1.221,
                         2.827,3.465,1.65,2.904,2.42,2.94,1.3])

plt.scatter(x, y)
plt.xlabel('Running Distance (Mile)')
plt.ylabel('Water Drinks (Litre)')

# Question 1
## For linear relationship, mean-square-error (MSE) tells if it is a good line (good model) or not
## y[i] and y_pred[i] are i-th element of list y and list y_pred respectively where y_pred[i] = w_1 x[i] +w_0
## Define error as: E[i] = y_pred[i] - y[i]
## Define mean-square-error as: MSE = 1/N sum_{i=0}^{N-1} E[i]^2
## Also mean-square-error is equal to: MSE = 1/N sum_{i=0}^{N-1} (y_pred[i] - y[i])^2
## The parameter N is: N = len(y)

def min_sq_error(y, x, w1, w0): #w1 = slope && w0 = intercept
    y_pred = [w1*num+w0 for num in x]
    # print(y_pred)
    sum_squared_error = sum([(y_element - f_element)**2 for y_element,f_element in zip(y,y_pred)])
    N = len(y)
    mse = sum_squared_error/N
    return mse

print(f'Mean Squared Error of (y, x, 0.7, 0.3) = {min_sq_error(y, x, 0.7, 0.3)}')
print(f'Mean Squared Error of (y, x, 0.25163494, 0.79880123) = {min_sq_error(y, x, 0.25163494, 0.79880123)}')
