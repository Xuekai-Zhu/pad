def solution():
    # Calculate the cost of buying a new computer and the cost of buying 2 used computers
    cost_new = 600
    cost_used = 2 * 200

    # Calculate the total lifespan of the new computer and the combined lifespan of the used computers
    lifespan_new = 6
    lifespan_used = 3

    # Calculate the cost per year for each option
    cost_per_year_new = cost_new / lifespan_new
    cost_per_year_used = cost_used / (2 * lifespan_used)

    # Calculate the amount saved by choosing the cheaper option
    if cost_per_year_new < cost_per_year_used:
        savings = cost_per_year_used * 6 - cost_new
    else:
        savings = cost_used - cost_per_year_new * 6

    result = savings
    return result

print(solution())