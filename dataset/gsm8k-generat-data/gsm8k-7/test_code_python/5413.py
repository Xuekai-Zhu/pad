def solution():
    num_peas = 56
    time_to_pick = 7

    # Calculate the rate at which Ben picks sugar snap peas
    rate = num_peas / time_to_pick

    # Use the rate to calculate how long it would take to pick 72 sugar snap peas
    num_peas_2 = 72
    time_to_pick_2 = num_peas_2 / rate
    result = time_to_pick_2
    return result

print(solution())