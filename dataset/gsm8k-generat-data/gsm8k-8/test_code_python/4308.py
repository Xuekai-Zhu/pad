def solution():
    # Define the cost of one roll
    cost_per_dozen = 5
    rolls_per_dozen = 12
    cost_per_roll = cost_per_dozen / rolls_per_dozen

    # Calculate the number of rolls John got
    total_cost = 15
    num_rolls = total_cost / cost_per_roll
    result = num_rolls
    return result

print(solution())