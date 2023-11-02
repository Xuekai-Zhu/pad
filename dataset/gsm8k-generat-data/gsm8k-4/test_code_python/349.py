def solution():
    """A farmer has twice as many pigs as cows, and 4 more cows than goats. If the farmer has 56 animals total, how many goats does he have?"""
    # Define the total number of animals
    total_animals = 56

    # Let's variable goats be x
    goats = None

    # calculate the number of cows
    cows = goats + 4

    # calculate the number of pigs
    pigs = 2 * cows

    # Calculate the total number of animals by adding up goats, cows, and pigs
    total = goats + cows + pigs

    # Check to make sure the total number of animals is the same as what was given
    while total != total_animals:
        # Increment the number of goats and recalculate
        goats += 1
        cows = goats + 4
        pigs = 2 * cows
        total = goats + cows + pigs

    # return the number of goats
    result = goats
    return result

print(solution())