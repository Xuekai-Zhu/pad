def solution():
    # Calculate the amount of water in the first 30 minutes
    water_in_30min = 2 * 3  # 2 cups per 10 minutes, for 30 minutes

    # Calculate the amount of water in the next 30 minutes
    water_in_60min = 2 * 6  # 2 cups per 10 minutes, for 60 minutes

    # Calculate the amount of water in the last hour
    water_in_last_hour = 4 * 6  # 4 cups per 10 minutes, for 60 minutes

    # Calculate the total amount of water
    total_water = water_in_30min + water_in_60min + water_in_last_hour

    # Calculate the amount of water to be dumped
    water_to_dump = total_water / 2

    # Calculate the amount of water left
    water_left = total_water - water_to_dump
    result = water_left
    return result

print(solution())