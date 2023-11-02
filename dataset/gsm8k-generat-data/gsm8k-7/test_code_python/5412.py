def solution():
    num_players = 30
    coach_water = 8 * 1000  # convert liters to milliliters
    water_per_player = 200
    water_spilled = 250

    # Calculate the total amount of water needed for all players
    total_water_needed = num_players * water_per_player

    # Calculate the remaining amount of water after the spill
    remaining_water = coach_water - total_water_needed - water_spilled
    result = remaining_water
    return result

print(solution())