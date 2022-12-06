#probability and entropy

import math
probability = .5

print(-math.log(probability, 2))

# [probability of a 0, probability of a 1]

p = [0.5, 0.5]

entropy_out = -sum([p_i * math.log(p_i, 2) for p_i in p])

print(entropy_out)

