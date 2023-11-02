def solution():
    """Sun City has 1000 more than twice as many people as Roseville City. Roseville city has 500 less than thrice as many people as Willowdale city. If Willowdale city has 2000 people, how many people live in Sun City?"""
    # Define the number of people in Willowdale city
    willowdale_pop = 2000

    # Calculate the number of people in Roseville city
    roseville_pop = 3 * willowdale_pop - 500

    # Calculate the number of people in Sun City
    suncity_pop = 2 * roseville_pop + 1000

    # Display the number of people in Sun City
    result = suncity_pop
    return result

print(solution())