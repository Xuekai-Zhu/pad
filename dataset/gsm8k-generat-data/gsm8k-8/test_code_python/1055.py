def solution():
    # Define the population of New England
    new_england_population = 2100000

    # Calculate the population of New York
    new_york_population = 2/3 * new_england_population

    # Calculate the combined population of both states
    total_population = new_england_population + new_york_population
    result = total_population
    return result

print(solution())