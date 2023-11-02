def solution():
    # Determine how many times John's hair grows 9 inches before he cuts it
    growth_period = (9 - 6) / 1.5

    # Calculate the total number of haircuts he gets in a year
    haircuts_per_year = 12 / growth_period

    # Calculate the cost of one haircut including the tip
    cost_per_haircut = 45 * 1.2

    # Calculate the total cost of haircuts in a year
    total_cost = haircuts_per_year * cost_per_haircut
    result = total_cost
    return result

print(solution())