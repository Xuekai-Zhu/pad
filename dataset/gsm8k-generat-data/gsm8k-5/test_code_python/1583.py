def solution():
    # Calculate the cost and lifespan of the new computer
    new_cost = 600
    new_lifespan = 6

    # Calculate the cost and lifespan of the used computers
    used_cost = 2 * 200
    used_lifespan = 3

    # Calculate the cost per year for each option
    new_cost_per_year = new_cost / new_lifespan
    used_cost_per_year = used_cost / (2 * used_lifespan)

    # Calculate the amount of money saved by picking the cheaper option
    savings = new_cost_per_year - used_cost_per_year
    result = savings
    return result

print(solution())