def solution():
    # Calculate the cost and lifespan of the new computer
    new_computer_cost = 600
    new_computer_lifespan = 6

    # Calculate the cost and lifespan of the used computers
    used_computer_cost = 2 * 200
    used_computer_lifespan = 3

    # Calculate the total cost per year for each option
    new_computer_cost_per_year = new_computer_cost / new_computer_lifespan
    used_computer_cost_per_year = used_computer_cost / (2 * used_computer_lifespan)

    # Calculate the total savings over the 6-year lifespan of the new computer 
    total_savings = (new_computer_cost_per_year * new_computer_lifespan) - (used_computer_cost_per_year * (2 * used_computer_lifespan))

    result = total_savings
    return result

print(solution())