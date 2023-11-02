def solution():
    """Sun City has 1000 more than twice as many people as Roseville City. Roseville city has 500 less than thrice as many people as Willowdale city. If Willowdale city has 2000 people, how many people live in Sun City?"""
    # Define the population of Willowdale city
    willowdale_population = 2000

    # Calculate the population of Roseville city
    roseville_population = 3 * willowdale_population - 500

    # Calculate the population of Sun City
    suncity_population = 2 * roseville_population + 1000

    # Return the population of Sun City
    result = suncity_population
    return result

print(solution())