def solution():
    num_windows = 3  # Laura needs to buy window treatments for 3 windows

    # Calculate the cost of sheers and drapes for each window
    cost_per_window = (40 + 60) * 2  # $40 for sheers, $60 for drapes, and 2 pairs per window

    # Calculate the total cost for all the windows
    total_cost = num_windows * cost_per_window
    result = total_cost
    return result

print(solution())