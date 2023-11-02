def solution():
    """Mike is feeding the birds at the park. He counts out the seeds as he throws them. He throws 20 seeds to the birds on the left. He throws twice as much to the bigger group of birds on the right. Some more birds flutter over to join the others for lunch and Mike throws 30 more seeds for them. If Mike has 30 seeds left to feed the last of the birds, how many seeds did Mike start with?"""
    # Calculate the number of seeds Mike threw to the birds on the left
    left_seeds = 20

    # Calculate the number of seeds Mike threw to the bigger group of birds on the right
    right_seeds = 2 * left_seeds

    # Calculate the total number of seeds thrown before the last group of birds arrived
    total_seeds = left_seeds + right_seeds

    # Calculate the total number of seeds thrown after the last group of birds arrived
    total_seeds += 30

    # Calculate the number of seeds Mike has left
    left_seeds = 30

    # Calculate the number of seeds Mike started with
    total_seeds += left_seeds

    # Display the number of seeds Mike started with
    result = total_seeds
    return result

print(solution())