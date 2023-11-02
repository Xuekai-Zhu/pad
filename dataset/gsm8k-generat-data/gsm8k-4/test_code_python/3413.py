def solution():
    """Mike is feeding the birds at the park. He counts out the seeds as he throws them. He throws 20 seeds to the birds on the left. He throws twice as much to the bigger group of birds on the right. Some more birds flutter over to join the others for lunch and Mike throws 30 more seeds for them. If Mike has 30 seeds left to feed the last of the birds, how many seeds did Mike start with?"""
    # Define the number of seeds Mike threw to the birds on the left
    seeds_left = 20

    # Define the number of seeds Mike threw to the birds on the right, which is twice the number of seeds he threw to the left
    seeds_right = seeds_left * 2

    # Define the number of seeds Mike threw for the extra birds that joined in
    seeds_extra = 30

    # Calculate the total number of seeds Mike threw
    total_seeds = seeds_left + seeds_right + seeds_extra + 30

    # Calculate the number of seeds Mike started with, by adding the seeds he had left to the total seeds he threw
    seeds_start = total_seeds + 30

    # Display the result
    result = seeds_start
    return result

print(solution())