def solution():
    """New York is two-thirds as populated as all of New England. If New England has 2100000 people, calculate the combined population of both states."""
    new_england_population = 2100000
    new_york_population = (2/3) * new_england_population
    total_population = new_england_population + new_york_population
    result = total_population
    return result

print(solution())