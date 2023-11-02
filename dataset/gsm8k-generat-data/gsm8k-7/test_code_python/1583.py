def solution():
    new_comp_cost = 600
    used_comp_cost = 200
    new_comp_life = 6
    used_comp_life = 3

    # Calculate the cost of buying a new computer and using it for 6 years
    new_comp_total_cost = new_comp_cost

    # Calculate the cost of buying 2 used computers and using them for 3 years each
    used_comp_total_cost = 2 * used_comp_cost

    # Calculate the total cost of the cheaper option
    cheaper_total_cost = min(new_comp_total_cost, used_comp_total_cost)

    # Calculate the amount saved by picking the cheaper option
    savings = abs(new_comp_total_cost + used_comp_total_cost - cheaper_total_cost)
    result = savings
    return result

print(solution())