import numpy as np

# somebody on discord was asking for a solution to the problem:

#  how can I get "True" when two numbers are CLOSE (distance = 1 between any two)
#  but then the THIRD number is FAR (distance > 1 from the pair with the distance 1)

# I came up with this solution:

def three_numbers_one_cup(numbers):
    numbers = numbers - np.median(numbers)
    numbers = np.abs(numbers)
    magic_constant = np.cumsum(numbers)

    return magic_constant.max()


for i in [[1, 2, 10], [1, 2, 3], [4, 1, 3], [0, 0, 10], [-1, -0.5, 3], [-1, -1, -1]]:
    s = np.array(i)

    print(sorted(s), three_numbers_one_cup(s), three_numbers_one_cup(s) >= 3)
