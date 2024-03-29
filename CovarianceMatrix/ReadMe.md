
# Samuel Folledo's Covariance Matrix Code
This method takes in a 2-dimensional array of any size in x or y and returns the covariance of a dataset in a form of a matrix, a.k.a. a 2D array

<img src="https://github.com/SamuelFolledo/Math-Functions/blob/master/screenshots/covariance.png" width="800" height="800">

## Covariance in Pen and Paper
<img src="https://github.com/SamuelFolledo/Math-Functions/blob/master/screenshots/covariance_sample.jpg" width="800" height="800">

## What Is Covariance?
__Covariance__ In probability theory and statistics, covariance is a measure of the joint variability of two random variables. Covariance measures the directional relationship between the returns on two assets. A positive covariance means that asset returns move together while a negative covariance means they move inversely. Covariance is calculated by analyzing at-return surprises (standard deviations from the expected return) or by multiplying the correlation between the two variables by the standard deviation of each variable.

### KEY TAKEAWAYS
- Covariance is a statistical tool that is used to determine the relationship between the movement of two asset prices.
- When two stocks tend to move together, they are seen as having a positive covariance; when they move inversely, the covariance is negative.
- Covariance is a significant tool in modern portfolio theory used to ascertain what securities to put in a portfolio.
- Risk and volatility can be reduced in a portfolio by pairing assets that have a negative covariance.


# [Instructions](https://github.com/Make-School-Courses/QL-1.1/blob/master/Assignments/HW1.ipynb)
## HW1 - Covariance Matrix
**Covariance** is used to measure how two random variables change or vary together. For example, the height and weight of giraffes have a positive covariance because when one is big, the other tends to also be big.
_In this assignment, we will calculate the **covariance matrix** for a given dataset._
    
This assignment will consist of two parts:

## Part 1

**IMPORTANT NOTE:** in the video, the equation he uses has n as the denominator, but when he calculates covariance values, he's using n-1 as the denominator. _For our purposes, we will be using n-1 as the denominator._

Watch this video on covariance matrices: https://www.youtube.com/watch?v=0GzMcUy7ZI0

Mathematically, we can represent Covariance as such:

`Cov(X,Y)=1/(n-1) \\sum_{i=1}^{n}(x[i] - \\bar{x})(y[i] - \\bar{y})`

Where n is the number of elements in arrays x and y

## Part 2

Write a Python function that returns the covariance matrix for a given dataset, just like we watched in the video or any other dataset of your choosing. Below are various places you can get datasets from:

### Dataset Resources

- [Kaggle](https://www.kaggle.com/datasets)
- [Fivethirtyeight](https://github.com/fivethirtyeight/data)
- [Buzzfeed News](https://github.com/BuzzFeedNews/everything)
- [Google Cloud BigQuery Public Datasets](https://cloud.google.com/bigquery/public-data/)
- [Wikipedia](https://en.wikipedia.org/wiki/Wikipedia:Database_download)
- Can't find anything from above? Google around until you do!

## Part 3

Use [numpy's var function](https://docs.scipy.org/doc/numpy/reference/generated/numpy.var.html) to confirm that the covariance between a variable and itself is the same as the variance of the variable.

For example, assuming your covariance function is named `cov`, ensure that the following is true: 
`cov(X, X) == np.var(X)`

### Hints

1. Obtain the covariance between columns x and y, between columns x and z, and columns y and z
1. The covariance between columns x and y is the same as the covariance between columns y and x. _We can generalize this for any two columns_
1. Show that the covariance between columns x and x is equal to the variance of column x. _We can generalize this for any other column_

# Requirements

To pass this HW, you must meet the following requirements

1. Your function should return the covariance between 6 pairs of random variables: (X,Y), (X, Z), (Y, Z), (X, X), (Y, Y), and (Z, Z)
1. Verify that your function's return value is correct by using `np.cov(DATA)` where `DATA` is the return value of your covariance function
1. Verify that your covariance function for each variable with itself returns the same value as `np.var` of that variable

## Stretch Challenges

These are optional challenges for those who want to further expand their skillset:

1. Your function should display the covariance in a matrix format

## Turning In Your HW

Once you have finished your assignment, provide a link to your repo on GitHub and place the link in the appropriate `HW1` column in the progress tracker. See the syllabus for more details on submission links
