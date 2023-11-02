def solution():
    """Mike is feeding the birds at the park. He counts out the seeds as he throws them. He throws 20 seeds to the birds on the left. He throws twice as much to the bigger group of birds on the right. Some more birds flutter over to join the others for lunch and Mike throws 30 more seeds for them. If Mike has 30 seeds left to feed the last of the birds, how many seeds did Mike start with?"""
    seeds_left = 30
    left_birds_seeds = 20
    right_birds_seeds = 2 * left_birds_seeds
    total_seeds = seeds_left + left_birds_seeds + right_birds_seeds + 30
    result = total_seeds
    return result

print(solution())