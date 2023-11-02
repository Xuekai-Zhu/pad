def solution():
    # Define the variables
    total_players = 30
    water_per_player = 200 # in milliliters
    coach_water = 8 * 1000 # in milliliters
    water_spill = 250 # in milliliters

    # Calculate the total amount of water needed
    total_water_needed = total_players * water_per_player

    # Subtract the amount of spilled water from the coach's water
    remaining_water = coach_water - water_spill

    # Subtract the total water needed from the remaining water
    water_leftover = remaining_water - total_water_needed
    result = water_leftover/1000 # convert to liters
    return result

print(solution())