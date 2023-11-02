def solution():
    num_pots = 3
    pot_price = 20

    num_pans = 4
    total_cost = 100

    # Calculate the total cost of all pots
    total_pots_cost = num_pots * pot_price

    # Calculate the total cost of all pans
    total_pans_cost = total_cost - total_pots_cost

    # Calculate the cost of one pan
    pan_price = total_pans_cost / num_pans

    # Calculate the cost of two pans
    two_pans_cost = pan_price * 2
    result = two_pans_cost
    return result

print(solution())