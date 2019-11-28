import numpy as np
import matplotlib.pyplot as plt

# Running dataset - Distance in Mile
x = np.array([3.3,4.4,5.5,6.71,6.93,4.168,9.779,6.182,7.59,2.167,
                         7.042,10.791,5.313,7.997,5.654,9.27,3.1])
# Water dataset -  Drinks in Litre
y = np.array([1.7,2.76,2.09,3.19,1.694,1.573,3.366,2.596,2.53,1.221,
                         2.827,3.465,1.65,2.904,2.42,2.94,1.3])

plt.scatter(x, y)
plt.xlabel('Running Distance (Mile)')
plt.ylabel('Water Drinks (Litre)')

w_1 = 0.25163494
w_0 = 0.79880123
y_pred = [w_1*i+w_0 for i in x]
plt.scatter(x, y)
plt.plot(x, y_pred, 'ro-')

def r_sq(y, x, w1, w0):
    y_bar  = np.mean(y)
    y_pred = [w1*num+w0 for num in x]
    SS_res = sum([(y_element - f_element)**2 for y_element,f_element in zip(y,y_pred)])
    SS_tot = sum([(y_element - y_bar)**2 for y_element in y])
    return 1- SS_res/SS_tot
print(r_sq(y, x, 0.25163494, 0.79880123))

# Verify that your function works correctly
from scipy import stats

slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
print("r-squared:", r_value**2)