def solution():
    # Calculate the number of seeds extracted from the apples, pears, and grapes
    apple_seeds = 4 * 6
    pear_seeds = 3 * 2
    grape_seeds = 9 * 3
    total_seeds = apple_seeds + pear_seeds + grape_seeds

    # Calculate the number of seeds needed to fulfill the assignment
    seeds_needed = 60 - total_seeds
    result = seeds_needed
    return result

print(solution())