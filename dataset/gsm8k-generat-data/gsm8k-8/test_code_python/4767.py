def solution():
    # Define the number of pots and pans
    num_pots = 3
    num_pans = 4

    # Define the cost of each pot and the total cost of all pots
    pot_cost = 20
    total_pot_cost = num_pots * pot_cost

    # Calculate the total cost of all pans
    total_pan_cost = 100 - total_pot_cost

    # Calculate the cost of one pan
    pan_cost = total_pan_cost / num_pans

    # Calculate the cost of 2 pans
    cost_of_two_pans = 2 * pan_cost
    result = cost_of_two_pans
    return result

print(solution())