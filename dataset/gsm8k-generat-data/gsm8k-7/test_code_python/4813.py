def solution():
    num_windows = 3
    sheer_price = 40.0
    drape_price = 60.0

    # Calculate the total cost of all sets of sheers
    total_sheer_cost = num_windows * sheer_price

    # Calculate the total cost of all sets of drapes
    total_drape_cost = num_windows * drape_price

    # Calculate the total cost of all window treatments
    total_cost = total_sheer_cost + total_drape_cost
    result = total_cost
    return result

print(solution())