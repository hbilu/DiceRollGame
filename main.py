
"""
Calculate the chance that you will reach 30th step of the Eiffel Tower under following conditions:
Throw a die 100 times
- If it is 1 or 2, you will go one step down.
- If it is 4 or 5, you will go one step up.
- If it is 3 or 6, you will throw the dice again:
	+ If it is 1 or 2, you will go one step down.
	+ If it is between 3-6, you will walk up the resulting number of steps.
- You cannot go down, if you are on the step 0.
- You have a chance of 0,1% of falling down the stairs.
"""

# importing numpy and matplotlib packages
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(111)
walk = []

for i in range(100000):
	random_walk = [0]
	for k in range(100):
		step = random_walk[-1]
		dice = np.random.randint(1, 7)
		if dice <= 2:
			# step does not go below zero (0) if dice is equal to 1 or 2
			step = max(0, step-1)
		elif dice > 3 or dice < 6:
			step = step+1
		else:
			dice2 = np.random.randint(1, 7)
			if dice2 <= 2:
				step = max(0, step-1)
			else:
				step = step+dice2
		# Calculate the chance of 0,1% of falling down the stairs
		# Generate a random float between 0 and 1.
		# If this value is less than or equal to 0.001, you should reset step to 0.
		if np.random.rand() <= 0.001:
			step = 0
		random_walk.append(step)
	walk.append(random_walk)

# np.array(walk).shape -> (100000, 101) ---- walk2.shape -> (101, 100000)
walk2 = np.transpose(np.array(walk))

# visualizing the first ten game
plt.plot(walk2[:, 0:10])
plt.xlim(0, 100)
plt.xlabel('step walks of the first 10 roll dice game')
plt.ylabel('stairs of the Eiffel Tower')
plt.show()
plt.clf()

# take final step of each 100 dice roll game
last_steps = walk2[-1, :]

# plotting a histogram to see the distribution
plt.hist(last_steps, bins=10)
plt.xlabel('final step reached by each 100 dice roll game')
plt.show()

# the chance (in percentage) to reach 30th step
print((np.sum(last_steps >= 30)/100000)*100)
print((np.count_nonzero(last_steps >= 30)/len(last_steps))*100)
