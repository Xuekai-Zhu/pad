def solution():
    # Define number of windows
    num_windows = 3

    # Define cost of sheers and drapes
    sheer_cost = 40.00
    drape_cost = 60.00

    # Calculate cost of window treatments
    total_cost = (sheer_cost + drape_cost) * 2 * num_windows
    result = total_cost
    return result

print(solution())