def solution():
    # Calculate the total amount of water in cups
    first_30_min = 2 * 3  # steady flow of 2 cups per 10 minutes for the first 30 minutes
    next_30_min = 2 * 3  # still flows at 2 cups per 10 minutes for the next 30 minutes after
    next_60_min = 4 * 6  # maximizes to 4 cups per 10 minutes for the next hour
    total_water = first_30_min + next_30_min + next_60_min  # total amount of water in cups

    # Calculate the amount of water left after dumping half
    water_left = total_water / 2
    result = water_left
    return result

print(solution())