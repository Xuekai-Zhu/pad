def solution():
    """Sun City has 1000 more than twice as many people as Roseville City. Roseville city has 500 less than thrice as many people as Willowdale city. If Willowdale city has 2000 people, how many people live in Sun City?"""
    willowdale_population = 2000
    roseville_population = 3 * willowdale_population - 500
    suncity_population = 2 * roseville_population + 1000
    result = suncity_population
    return result

print(solution())