def solution():
    """Steven's teacher sends the class an assignment to collect 60 different fruit seeds. Apples average 6 seeds, pears average 2 seeds, and grapes average 3 seeds. Steven has set aside 4 apples, 3 pears, and 9 grapes to extract their seeds. How many more seeds does he need to fulfill his assignment?"""
    # Define the average number of seeds per fruit
    APPLE_SEEDS = 6
    PEAR_SEEDS = 2
    GRAPE_SEEDS = 3

    # Define the number of each type of fruit Steven has set aside
    apples = 4
    pears = 3
    grapes = 9

    # Calculate the total number of seeds from the fruit Steven has set aside
    total_seeds = (apples * APPLE_SEEDS) + (pears * PEAR_SEEDS) + (grapes * GRAPE_SEEDS)

    # Calculate the number of seeds Steven still needs to collect
    remaining_seeds = 60 - total_seeds

    # Display the number of seeds Steven still needs to collect
    result = remaining_seeds
    return result

print(solution())