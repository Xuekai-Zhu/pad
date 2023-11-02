def solution():
    """Hannah's family has ten pigs on their farm. They also have three fewer than twice as many cows as pigs and six more goats than cows. How many animals do they have on their farm?"""
    # Define the initial number of pigs
    pigs = 10

    # Define the number of cows as twice the number of pigs minus 3
    cows = 2 * pigs - 3

    # Define the number of goats as the number of cows plus 6
    goats = cows + 6

    # Calculate the total number of animals
    total_animals = pigs + cows + goats

    # return the result
    result = total_animals
    return result

print(solution())