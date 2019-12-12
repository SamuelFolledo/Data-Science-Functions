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

############################################################################
###################################### Question 1 ######################################
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

#########################################################################################
####################################### Question 3 ######################################
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

########################################################################################
###################################### Question 4 ######################################
# ERRORS Error[i] = y_pred[i] - y[i] 
errors = [(i-j) for i, j in zip(y, predicted_y_values)] #Error = vertical distance between y and y_pred
print(f'\nERRORS = {errors}')
# VARIANCE of errors
errors_variance = np.var(errors, ddof=1)
print(f'\nVARIANCE of errors = {errors_variance}')
# MEAN of errors
errors_mean = get_mean(errors)
print(f'\nMEAN of errors = {errors_mean}')

# PLOT
sns.distplot(errors, hist=True, kde=False, bins=8)
plt.title('Error Value and Frequency Histogram of Error[i] = y_pred[i] - y[i]',fontsize=24)
plt.xlabel('Error Value',fontsize=16)
plt.ylabel('Frequency',fontsize=16)

#PLOT with KDE = True
sns.distplot(errors, hist=True, kde=True, bins=4)
plt.title('Error Value and Frequency Histogram with KDE of Error[i] = y_pred[i] - y[i]',fontsize=24)
plt.xlabel('Error Value',fontsize=16)
plt.ylabel('Frequency',fontsize=16)

#########################################################################################
###################################### Question #5 ######################################
w_0 = np.random.randn()
w_1 = np.random.randn()
step = 0.01
epoch = 5000 #we are assuming that iteration is 5000, that's why we use while loop in the next example

# From slope_intercept_LR method
x_bar = get_mean(x)
y_bar = get_mean(y)
x_y_bar = sum([(i*j) for i,j in zip(x,y)]) / len(x)
x_squared_bar = sum([i**2 for i in x]) / len(x)

for _ in range(epoch):
    w_1 = w_1 - step * (w_1*x_squared_bar + w_0*x_bar - x_y_bar)
    w_0 = w_0 - step * (w_1*x_bar + w_0 - y_bar)
print(w_1)
print(w_0)

# Test Question 5
from scipy import stats
print(stats.linregress(x, y))


##################################################################################################################
##################################################################################################################
# Milad's better solution for Question #5 optional reading
# It is better to have while loop, if |J(w1,w0) at n+1 ietration - J(w1,w0) at n ietration|<=eps stop the while loop
import numpy as np
# Running Distance in Mile
x = np.array([3.3,4.4,5.5,6.71,6.93,4.168,9.779,6.182,7.59,2.167,
                         7.042,10.791,5.313,7.997,5.654,9.27,3.1])
# Water Drinks in Litre
y = np.array([1.7,2.76,2.09,3.19,1.694,1.573,3.366,2.596,2.53,1.221,
                         2.827,3.465,1.65,2.904,2.42,2.94,1.3])
N = len(y)
xx_bar = np.mean([i*i for i in x])
xy_bar = np.mean([i*j for i, j in zip(x, y)])                  
x_bar = np.mean(x)
y_bar = np.mean(y) 
w_0 = np.random.randn()
w_1 = np.random.randn()
iteration = 0 
while True if iteration == 0 else np.abs(E2 - E1) >= 0.000000001: #this infinite loop will stop if 'np.abs(E2 - E1) >= 0.000000001' == false
    y_pred = [w_1*i + w_0 for i in x]
    error  = [(i-j) for i,j in zip(y_pred, y)]
    sum_squared_error = sum([(i-j)**2 for i,j in zip(y_pred, y)])
    E1 = sum_squared_error/N 
    w_1 = w_1 - 0.01*(2*w_1*xx_bar + 2*w_0*x_bar-2*xy_bar)
    w_0 = w_0 - 0.01*(2*w_1*x_bar+2*w_0-2*y_bar)  
    y_pred = [w_1*i + w_0 for i in x]
    error  = [(i-j) for i,j in zip(y_pred, y)]
    sum_squared_error = sum([(i-j)**2 for i,j in zip(y_pred, y)])
    E2 = sum_squared_error/N 
    iteration += 1
print(w_1)
print(w_0)
print(iteration)