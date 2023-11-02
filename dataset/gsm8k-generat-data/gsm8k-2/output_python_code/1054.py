def solution():
    """New York is two-thirds as populated as all of New England. If New England has 2100000 people, calculate the combined population of both states."""
    new_england_pop = 2100000
    ny_pop = (2/3) * new_england_pop
    total_pop = new_england_pop + ny_pop
    result = total_pop
    return result

print(solution())