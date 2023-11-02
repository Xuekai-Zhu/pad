def solution():
    num_previous_bales = 10
    previous_cost_per_bale = 15
    num_new_bales = 20
    new_cost_per_bale = 18

    # Calculate the total cost of the previous bales of hay
    previous_total_cost = num_previous_bales * previous_cost_per_bale

    # Calculate the total cost of the new bales of hay
    new_total_cost = num_new_bales * new_cost_per_bale

    # Calculate the difference in cost between the previous and new bales of hay
    cost_difference = new_total_cost - previous_total_cost
    result = cost_difference
    return result

print(solution())