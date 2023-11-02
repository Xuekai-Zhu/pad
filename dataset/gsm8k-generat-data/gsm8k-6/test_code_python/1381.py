def solution():
    # Calculate the total amount of water used to fill the bathtub
    total_water = 120 * 14  # Each bucket holds 120 ounces, and he filled the bathtub 14 times
    water_level = 120 * 11  # To get to the level he puts it at, he needs to take away 3 buckets (120 * 3)
    water_used = total_water - water_level  # Calculate the amount of water used for his bath

    # Calculate the amount of water he uses each week
    water_weekly = water_used * 7  # He takes a bath every day
    result = water_weekly
    return result

print(solution())