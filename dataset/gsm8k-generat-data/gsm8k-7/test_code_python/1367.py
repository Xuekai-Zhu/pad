def solution():
    total_backers = 2 + 3 + 10

    # Set up system of equations with three unknowns
    # Let x be the amount of money raised at the lowest level
    # Then the amount of money raised at the other two levels are 10x and 100x, respectively
    # The sum of these amounts equals $12000
    # The number of backers at each level can be used to set up additional equations
    # Using this information, we can solve for x and find the amount raised at the highest level
    x = 120 / (total_backers + 9)  # Using substitution to solve for x
    highest_level = 100 * x
    
    result = highest_level
    return result

print(solution())