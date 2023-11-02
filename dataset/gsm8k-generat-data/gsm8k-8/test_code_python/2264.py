def solution():
    # Calculate the number of people in Willowdale city
    willowdale_population = 2000

    # Calculate the number of people in Roseville city
    roseville_population = 3 * willowdale_population - 500

    # Calculate the number of people in Sun City
    suncity_population = 2 * roseville_population + 1000

    result = suncity_population
    return result

print(solution())