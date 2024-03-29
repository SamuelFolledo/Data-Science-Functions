# Final Project

## [Instructions](https://github.com/Make-School-Courses/QL-1.1/blob/master/Final_Project/Final_Project.ipynb)

## Code Snippet
```
import numpy as np
import matplotlib.pyplot as plt

# Running Distance in Mile
x = np.array([3.3,4.4,5.5,6.71,6.93,4.168,9.779,6.182,7.59,2.167,7.042,10.791,5.313,7.997,5.654,9.27,3.1])
# Water Drinks in Litre
y = np.array([1.7,2.76,2.09,3.19,1.694,1.573,3.366,2.596,2.53,1.221, 2.827,3.465,1.65,2.904,2.42,2.94,1.3])

# Question 1
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
```

## Final Project: Linear Regression
	•	We want to present the relationship between (two) variables linearly 
	•	For example, recall the running distance and drinking water 
	•	We are interested to obtain the best line describing by y_pred[i] = w_1 x[i] +w_0 that maps running distance to drinking water 
	•	Below, list x represents running distance in miles and list y represents the drinking water in litres 

## Questions
### Question 1: Obtain the MSE for the following two lines:
1- y_pred[i] = 0.7*x[i] + 0.3
2- y_pred[i] = 0.25163494*x[i] + 0.79880123
Hint: Your function take four input arguments: 1- y, 2- x, 3- slope, 4-intercept
In [ ]:
def min_sq_error(y, x, w1, w0):
    y_pred = ...
    sum_squared_error = ...
    N = len(y)
    mse = sum_squared_error/N
    return mse

print(min_sq_error(y, x, 0.7, 0.3))
print(min_sq_error(y, x, 0.25163494, 0.79880123))


### Question 2: Obtain the best line (Coding is not required)
	•	In order the best line, we want to obtain which slope (￼) and intercept (￼) minimize the mean-square-error (MSE) 
	•	For this part, you need to use partial derivative and you use derivative table 
	•	For this part, write down the steps and the solution on a paper

<img src="https://github.com/SamuelFolledo/Math-Functions/blob/master/screenshots/bestLine.jpg" width="727" height="1276">

### Question 3: Write a code to return the slope and intercept with given list x and y
	
In [ ]:
def slope_intercept_LR(x, y):
    w1 = ...
    w0 = ...
    return w1, w0

print(slope_intercept_LR(x, y))

### Question 4: After obtain the best line, obtain the variance and mean of error
	•	In Question 3, we have obtained the best line
	•	So, we can error list which its element is: ￼
	•	Write a function that calculate variance and mean of list ￼
	•	Plot the distribution of the error for optimal line


### Question 5: (Optional but Bonus point) In almost all applications, we update the slope and intercept through iteration
	•	Instead of putting the ￼ ￼
	▪	Initialize the ￼ and ￼ with arbitrary value, then update them by follwing Gradient Updating Rule:
	▪	￼
	▪	￼
In [ ]:
import numpy as np

w_0 = np.random.randn()
w_1 = np.random.randn()
step = 0.01
epoch = 5000
for _ in range(epoch):
    w_1 = w_1 - step*...
    w_0 = w_0 - step*...
print(w_1)
print(w_0)
