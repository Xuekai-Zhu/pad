def solution():
    """A farmer has twice as many pigs as cows, and 4 more cows than goats. If the farmer has 56 animals total, how many goats does he have?"""
    # Define the number of cows relative to goats
    COWS_PER_GOAT = 4

    # Define the total number of animals
    total_animals = 56

    # Set up the system of equations
    # Let x be the number of goats
    # Then the number of cows is x/COWS_PER_GOAT + 4
    # And the number of pigs is twice the number of cows, or 2(x/COWS_PER_GOAT + 4)
    # The total number of animals is the sum of goats, cows, and pigs, or x + x/COWS_PER_GOAT + 4 + 2(x/COWS_PER_GOAT + 4)
    # Simplifying the equation, we get 5x/4 + 12 = total_animals
    # Solving for x, we get x = (total_animals - 12)*4/5

    goats = int((total_animals - 12)*4/5) # round down to the nearest integer

    # Display the number of goats
    result = goats
    return result

print(solution())