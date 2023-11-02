def solution():
    """There are 30 players on a football team. The coach has 8 liters of water. She pours 200 milliliters of water for every player so they can get hydrated. Unfortunately, there was a water spill and 250ml of water was spilled. How much water was left over?"""
    players = 30
    water_per_player = 200/1000 # convert ml to liters
    total_water_needed = players * water_per_player
    water_left = 8 - total_water_needed - 250/1000 # convert ml to liters
    result = water_left
    return result

print(solution())