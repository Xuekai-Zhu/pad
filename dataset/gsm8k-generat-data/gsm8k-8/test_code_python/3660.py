def solution():
    # Define the unit profit
    unit_profit = 5 - (0.8 * 5)

    # Calculate the number of ice cream cones needed to make a $200 profit
    num_cones_needed = 200 / unit_profit
    result = num_cones_needed
    return result

print(solution())