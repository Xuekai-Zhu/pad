def solution():
    """There are 30 players on a football team. The coach has 8 liters of water. She pours 200 milliliters of water for every player so they can get hydrated. Unfortunately, there was a water spill and 250ml of water was spilled. How much water was left over?"""
    # Define the number of players and the amount of water per player
    num_players = 30
    water_per_player = 200 # in milliliters

    # Calculate the total amount of water needed for all players
    total_water = num_players * water_per_player # in milliliters
    total_water_liters = total_water / 1000 # convert to liters

    # Subtract the amount of spilled water from the total amount of water
    remaining_water_liters = 8 - (250 / 1000) - total_water_liters

    # Display the remaining amount of water
    result = remaining_water_liters
    return result

print(solution())