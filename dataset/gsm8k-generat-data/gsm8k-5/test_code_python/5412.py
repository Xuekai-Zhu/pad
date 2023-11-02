def solution():
    num_players = 30
    water_per_player = 200  # in milliliters
    total_water = 8 * 1000  # convert liters to milliliters
    total_water_used = num_players * water_per_player
    total_water_spilled = 250

    # Calculate the total water left over after spillage
    total_water_left = total_water - total_water_used - total_water_spilled
    result = total_water_left
    return result

print(solution())