def solution():
    """There are 30 players on a football team. The coach has 8 liters of water. She pours 200 milliliters of water for every player so they can get hydrated. Unfortunately, there was a water spill and 250ml of water was spilled. How much water was left over?"""
    total_players = 30
    water_per_player = 0.2
    total_water = 8
    water_spilled = 0.25
    total_water_needed = total_players * water_per_player
    remaining_water = total_water - total_water_needed - water_spilled
    result = remaining_water
    return result

print(solution())