# Coefficient of Determination (a.k.a. R-Squared) for Linear Regression
__Coefficient of Determination__ is the proportion of the variance in the dependent variable that is predictable from the independent variable(s).

It is a statistic used in the context of statistical models whose main purpose is either the prediction of future outcomes or the testing of hypotheses, on the basis of other related information. It provides a measure of how well observed outcomes are replicated by the model, based on the proportion of total variation of outcomes explained by the model

## Notes
- fi = Ypred[i]
- ```SStot = sum((Yi - mean(Y))^2)``` __total sum of squares__ - proportional to the [variance](https://en.wikipedia.org/wiki/Variance) of the data;
    - also known as __sum of squared residuals (SSR)__ or __(SSE)__ is a quantity that appears as part of a standard way of presenting results of such analyses. It is defined as being the sum, over all observations, of the squared differences between the observations and their overall mean
- ```SSreg = sum((Ypred[i] - mean(Y))^2)``` __regression sum of squares__ - also called the [explained sum of squares](https://en.wikipedia.org/wiki/Explained_sum_of_squares), is a quantity used in describing how well a model represents the data being modelle
- ```SStot = sum((Yi - Ypred[i])^2)``` __sum of squares of residuals__ - also called the [residual sum of squares](https://en.wikipedia.org/wiki/Residual_sum_of_squares), is the sum of the squares of residuals (deviations predicted from actual empirical values of data). It is a measure of the discrepancy between the data and an estimation model. 
- R-Squared or definition of the __coefficient of determination__ is:
    ```
    R^2 = 1 - (SSres / SStot)
    ```

Coefficient of determination. The coefficient of determination (R2) for a linear regression model with one independent variable is:
`R2 = { ( 1 / N ) * Σ [ (xi - x) * (yi - y) ] / (σx * σy ) }2`

where N is the number of observations used to fit the model, Σ is the summation symbol, xi is the x value for observation i, x is the mean x value, yi is the y value for observation i, y is the mean y value, σx is the standard deviation of x, and σy is the standard deviation of y.


HW3 - R-Squared for Linear Regression for my Data Science 1.0 course in Make School

https://github.com/Make-School-Courses/QL-1.1/blob/master/Assignments/HW3.ipynb

## Part 1
- Read [this wiki page about R-squared](https://en.wikipedia.org/wiki/Coefficient_of_determination#Definitions)

## Part 2
- Write a Python function that computes R-squared for our distance and drinking water datasets (shown at the top of this page) when w_1 = 0.25163494 and w_0 = 0.79880123
