def solution():
    tub_size = 120  # The tub has a capacity of 120 liters
    water_lost_per_cycle = 1  # 1 liter of water is lost per cycle
    flow_rate = 12  # The flow rate of the tap is 12 liters per minute

    # Calculate the time it takes to fill half the tub (60 liters)
    time_to_fill_half = 0
    water_in_tub = 0
    while water_in_tub < 60:
        water_in_tub += flow_rate - water_lost_per_cycle
        time_to_fill_half += 2  # Add both open and closed cycles

    # Calculate the total time to fill the tub
    total_time = time_to_fill_half * 2 - 1  # Subtract 1 because the last cycle won't complete
    result = total_time
    return result

print(solution())