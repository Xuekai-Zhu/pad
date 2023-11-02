def solution():
    """Mike is feeding the birds at the park. He counts out the seeds as he throws them. He throws 20 seeds to the birds on the left. He throws twice as much to the bigger group of birds on the right. Some more birds flutter over to join the others for lunch and Mike throws 30 more seeds for them. If Mike has 30 seeds left to feed the last of the birds, how many seeds did Mike start with?"""
    left_birds = 20
    right_birds = left_birds * 2
    total_birds = left_birds + right_birds
    extra_birds = 30
    last_birds = 30
    total_seeds = left_birds + (right_birds * 2) + extra_birds + last_birds
    starting_seeds = total_seeds + 30
    result = starting_seeds
    return result

print(solution())