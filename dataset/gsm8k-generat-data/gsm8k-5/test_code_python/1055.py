def solution():
    population_new_england = 2100000  # New England has 2.1 million people
    population_new_york = population_new_england * (2/3)  # New York is two-thirds as populated as New England

    # Calculate the combined population of both states
    total_population = population_new_england + population_new_york
    result = total_population
    return result

print(solution())