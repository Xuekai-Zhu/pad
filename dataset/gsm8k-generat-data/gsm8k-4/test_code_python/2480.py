def solution():
    """A school choir needs robes for each of its 30 singers. Currently, the school has only 12 robes so they decided to buy the rest. If each robe costs $2, how much will the school spend?"""
    # Define the number of robes needed and the cost per robe
    num_robes_needed = 30
    robe_cost = 2

    # Calculate the number of additional robes needed
    num_additional_robes_needed = num_robes_needed - 12

    # Calculate the total cost of the additional robes
    total_cost = num_additional_robes_needed * robe_cost

    result = total_cost
    return result

print(solution())