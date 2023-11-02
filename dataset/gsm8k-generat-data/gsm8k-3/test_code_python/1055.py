def solution():
    """New York is two-thirds as populated as all of New England. If New England has 2100000 people, calculate the combined population of both states."""
    # Calculate the population of New York
    ny_population = (2/3) * 2100000

    # Calculate the combined population of both states
    total_population = ny_population + 2100000

    # Display the total population
    result = total_population
    return result

print(solution())