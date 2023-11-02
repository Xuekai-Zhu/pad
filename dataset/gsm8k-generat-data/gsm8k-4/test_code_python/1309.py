def solution():
    """Martin has 18 goldfish. Each week 5 goldfish die. Martin purchases 3 new goldfish every week. How many goldfish will Martin have in 7 weeks?"""
    # Define the initial number of goldfish and the number of goldfish that die each week
    INITIAL_GOLDFISH = 18
    GOLDFISH_DEATH = 5

    # Define the number of goldfish purchased each week and the number of weeks
    GOLDFISH_PURCHASE = 3
    WEEKS = 7

    # Calculate the number of goldfish Martin will have after 7 weeks
    goldfish = INITIAL_GOLDFISH
    for week in range(WEEKS):
        # Subtract the number of goldfish that die each week
        goldfish -= GOLDFISH_DEATH

        # Add the number of goldfish purchased each week
        goldfish += GOLDFISH_PURCHASE

    # Return the result
    result = goldfish
    return result

print(solution())