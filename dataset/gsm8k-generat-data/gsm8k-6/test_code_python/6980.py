def solution():
    # Calculate the total number of remaining donuts
    remaining_donuts = 50 - 2 - 4  # Bill eats 2 donuts, secretary takes away 4 donuts
    remaining_donuts = remaining_donuts / 2  # coworkers steal half of the remaining donuts
    result = remaining_donuts
    return result

print(solution())