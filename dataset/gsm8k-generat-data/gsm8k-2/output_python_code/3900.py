def solution():
    """Steven's teacher sends the class an assignment to collect 60 different fruit seeds. Apples average 6 seeds, pears average 2 seeds, and grapes average 3 seeds. Steven has set aside 4 apples, 3 pears, and 9 grapes to extract their seeds. How many more seeds does he need to fulfill his assignment?"""
    apple_seeds = 6
    pear_seeds = 2
    grape_seeds = 3
    collected_apple_seeds = 4 * apple_seeds
    collected_pear_seeds = 3 * pear_seeds
    collected_grape_seeds = 9 * grape_seeds
    total_seeds_collected = collected_apple_seeds + collected_pear_seeds + collected_grape_seeds
    seeds_left = 60 - total_seeds_collected
    result = seeds_left
    return result

print(solution())