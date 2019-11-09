# Samuel Folledo's Probability Code
- 

## [What is Probability?](https://github.com/Make-School-Courses/QL-1.1/blob/master/Notebooks/Probability.ipynb)
Probability is all about the chances of an event occurring or how likely an event is to occur, in a set of events.

## [How to Interpret Probability](https://stattrek.com/probability/what-is-probability.aspx)
Mathematically, the probability that an event will occur is expressed as a number between 0 and 1. Notationally, the probability of event A is represented by P(A).

- If P(A) equals zero, event A will almost definitely not occur.
- If P(A) is close to zero, there is only a small chance that event A will occur.
- If P(A) equals 0.5, there is a 50-50 chance that event A will occur.
- If P(A) is close to one, there is a strong chance that event A will occur.
- If P(A) equals one, event A will almost definitely occur.
- In a statistical experiment, the sum of probabilities for all possible outcomes is equal to one. This means, for example, that if an experiment can have three possible outcomes (A, B, and C), then P(A) + P(B) + P(C) = 1.



# [HW2 - Probability Instructions](https://github.com/Make-School-Courses/QL-1.1/blob/master/Assignments/HW2.ipynb):

In this assignment, we will calculate the chance of getting a specific outcome from probabilistic events on piece of paper and then write a function to verify that our paper calculations are correct.

## Problem To Solve 

We have a coin that we want to flip. We know the following about the coin:

- The probability of getting a 'Head' is P(H) = a
- The probability of getting a 'Tail' is P(T) = 1 - a

a can be any decimal number between 0 and 1. For example, if a = 0.5, then it is a fair coin.

**Given the above probabilities for P(H) and P(T), if we toss this coin three times, what is the probability that we get some combination of two heads and one tail?**

## Part 1 - Paper Calculation

Calculate this probability on a piece of paper. Show your answer in terms of a

_Make sure to show your work, and when you're finished, take a picture to upload to your GitHub repo_


## Part 2

Write a function `verify_head` that we will use to verify if your paper solution is correct. Your function should have two parameters: 
    
- `prob_head`: Probability of getting a 'Head' (type: `float`)
- `num_flips`: Number of times we flip the coin (type: `integer`)

**Your function should then return the probability (float) of tossing a coin `num_flips` times and getting some combination of two heads and one tail, given that we know the probability of getting a heads is `prob_head`**


## Requirements

To pass this assignment, you must fulfuill the following requirements:

1. You must upload a picture of your own, original work showing how you calculated the probability of getting two heads
1. Your function must take in two parameters: the probability of getting Heads, and the number of flips.
1. Your function must return the correct decimal number (float) that corresponds to the probability of getting the input number of heads based on the input number of trials
    1. Note that your return value may differ slightly from the hand-calculated value, but they should be at least the same for the first 1-2 decimals if you use a `num_flips` value between 1000-2000


## Turning In Your HW

Once you have finished your assignment, provide a link to your repo on GitHub and place the link in the appropriate HW2 column in the progress tracker. See the syllabus for more details on submission links


## Hints: 

- Using a `num_flips` of 1000 (or higher!) is a good test number, as the probability will better align with what you get in your hand-calculated value
- For Part 2, we can generate events with given probabilities as follows. Think about how you could use this for your function:

    ['T']
    ['H']
    ['T']
    ['H']
    ['H']
    ['H']
    ['T']
    ['T']
    ['H']
    ['T']

```
from random import choices

event = ['H', 'T']
# Here we are saying the probability of getting Heads is 0.3,
# and that the probability of getting Tails is 0.7
weights = [0.3, 0.7]

for _ in range(10):
    print(choices(event, weights))
    
# Look at the below print statement.
# The number of Heads should be roughly 30%
# and the number of Tails should be roughly 70%
# You can change the range above to get more values,
# and see the percentage increase
```