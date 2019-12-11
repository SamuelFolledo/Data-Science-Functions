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

def get_mean(arr):
    return sum([i for i in arr]) / len(arr)

#Question 3
def slope_intercept_LR(x, y): #method which obtains the best line
    x_bar = get_mean(x)
    y_bar = get_mean(y)
    x_y_bar = sum([(i*j) for i,j in zip(x,y)]) / len(x)
    x_squared_bar = sum([i**2 for i in x]) / len(x)
    x_bar_squared = x_bar**2
    w1 = (x_y_bar - y_bar*x_bar) / (x_squared_bar - x_bar_squared)
    w0 = y_bar - w1*x_bar
    return w1, w0

print(f'w1 and w0 = {slope_intercept_LR(x, y)}')

#Question 4
y_variance = sum([(i - get_mean(y))**2 for i in y]) / len(y)
print(f'y_variance = {y_variance}')