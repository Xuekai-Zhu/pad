def solution():
    # Calculate the amount of water in the first 30 minutes
    first_half = 2 * 3  # 2 cups per 10 minutes, 3 times
    # Calculate the amount of water in the second 30 minutes
    second_half = 2 * 3  # 2 cups per 10 minutes, 3 times
    # Calculate the amount of water in the next hour
    next_hour = 4 * 6  # 4 cups per 10 minutes, 6 times
    # Calculate the total amount of water
    total_water = first_half + second_half + next_hour
    # Calculate how much water should be dumped
    dumped_water = 0.5 * total_water
    # Calculate the remaining amount of water
    remaining_water = total_water - dumped_water
    result = remaining_water
    return result

print(solution())