
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