# Final Project

## [Instructions]()

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

￼
	•	For this part, you need to use partial derivative and you use derivative table 
	•	For this part, write down the steps and the solution on a paper



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
