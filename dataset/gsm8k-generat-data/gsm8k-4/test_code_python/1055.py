def solution():
    """New York is two-thirds as populated as all of New England. If New England has 2100000 people, calculate the combined population of both states."""
    # Define the population of New England
    new_england_population = 2100000

    # Calculate the population of New York
    new_york_population = (2/3) * new_england_population

    # Calculate the combined population of both states
    combined_population = new_england_population + new_york_population

    # Return the result
    result = combined_population
    return result

print(solution())