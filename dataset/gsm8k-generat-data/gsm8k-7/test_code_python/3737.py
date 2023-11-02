def solution():
    num_barrels = 4
    barrel_capacity = 7
    flow_rate = 3.5

    # Calculate the total amount of water needed to fill all barrels
    total_water_needed = num_barrels * barrel_capacity

    # Calculate the time it will take to fill all barrels
    time_in_minutes = total_water_needed / flow_rate
    result = time_in_minutes
    return result

print(solution())