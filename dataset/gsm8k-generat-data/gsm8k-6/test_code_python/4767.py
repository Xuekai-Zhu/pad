def solution():
    # Calculate the total cost of the pots
    pot_cost = 3 * 20

    # Calculate the cost of the pans
    total_cost = 100
    pan_cost = (total_cost - pot_cost) / 4

    # Calculate the cost of 2 pans
    cost_of_2_pans = 2 * pan_cost
    result = cost_of_2_pans
    return result

print(solution())