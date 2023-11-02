def solution():
    water_per_day = 2.5
    num_days = 4
    bottle_size = 2

    # Calculate total water needed in liters
    total_water = water_per_day * num_days

    # Calculate number of bottles needed
    num_bottles = total_water / bottle_size

    result = num_bottles
    return result

print(solution())