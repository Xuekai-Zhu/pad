def solution():
    """Steven's teacher sends the class an assignment to collect 60 different fruit seeds. Apples average 6 seeds, pears average 2 seeds, and grapes average 3 seeds. Steven has set aside 4 apples, 3 pears, and 9 grapes to extract their seeds. How many more seeds does he need to fulfill his assignment?"""
    # Define the number of seeds in each fruit
    apple_seeds = 6
    pear_seeds = 2
    grape_seeds = 3

    # Define the number of each fruit that Steven has
    apples = 4
    pears = 3
    grapes = 9

    # Calculate the total number of seeds from the fruits Steven has
    total_seeds = (apples * apple_seeds) + (pears * pear_seeds) + (grapes * grape_seeds)

    # Calculate the number of additional seeds Steven needs to collect
    additional_seeds = 60 - total_seeds

    # return the result
    result = additional_seeds
    return result

print(solution())