
from random import choices
import numpy as np

event = ['H', 'T']

# Here we are saying the probability of getting Heads is 0.3,
# and that the probability of getting Tails is 0.7
weights = [0.5, 0.5]

results = []
for _ in range(3):
    result = choices(event, weights)[0] #choices() Return a k sized list of population elements chosen with replacement. If the relative weights or cumulative weights are not specified, the selections are made with equal probability.
    results.append(result)



# Look at the below print statement.
# The number of Heads should be roughly 30%
# and the number of Tails should be roughly 70%
# You can change the range above to get more values,
# and see the percentage increase

def coin_probability(coin_fairness, turns):
    event = ['H', 'T']
    weights = [coin_fairness, abs(1-coin_fairness)] #[0:P(H), 1:P(T)]
    results = []
    count = 0
    for _ in range(turns):
        result = choices(event, weights=weights, k=3) #k flips the coin 3x each turn
        results.append(result) #so we can check the result
        possible_results = [["H","H","T"], ["H","T","H"], ["T","H","H"]]
        if result in possible_results: #compare with accepted results
            count+=1
    return count/turns



print(coin_probability(0.1,10))


'''
choices()
Parameter	    Description
sequence	    Required. A sequence like a list, a tuple, a range of numbers etc.
weights	        Optional. A list were you can weigh the possibility for each value. Default None
cum_weights	    Optional. A list were you can weigh the possibility for each value, only this time the possibility is accumulated. Example: normal weights list: [2, 1, 1] is the same as this cum_weights list; [2, 3, 4]. Default None
k	            Optional. An integer defining the length of the returned list
'''




######## DICE #########
def roll_dice(size):
    dice = np.random.randint(low=1.0, high=7.0, size=size)
    print(dice)
    print(np.mean(dice))

'''
def randint(low, high=None, size=None, dtype='l')
Return random integers from low (inclusive) to high (exclusive).
Return random integers from the "discrete uniform" distribution of the specified dtype in the "half-open" interval [low, high). If high is None (the default), then results are from [0, low).
'''