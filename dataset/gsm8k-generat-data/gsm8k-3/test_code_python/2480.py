def solution():
    """A school choir needs robes for each of its 30 singers. Currently, the school has only 12 robes so they decided to buy the rest. If each robe costs $2, how much will the school spend?"""
    # Define the number of robes the school needs to buy and the cost per robe
    robes_needed = 30 - 12
    robe_cost = 2

    # Calculate the total cost of the robes
    total_cost = robes_needed * robe_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())