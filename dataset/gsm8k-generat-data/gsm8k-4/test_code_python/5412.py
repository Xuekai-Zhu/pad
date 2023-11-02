def solution():
    """There are 30 players on a football team. The coach has 8 liters of water. She pours 200 milliliters of water for every player so they can get hydrated. Unfortunately, there was a water spill and 250ml of water was spilled. How much water was left over?"""
    # Define the number of players and the amount of water the coach has
    num_players = 30
    water = 8

    # Calculate the amount of water needed for all players
    total_water = num_players * 0.2

    # Subtract the water spilled from the total water needed
    total_water -= 0.25

    # Subtract the total water needed from the initial amount of water
    remaining_water = water - total_water

    # Convert the remaining water to milliliters
    remaining_water *= 1000

    # Return the result
    result = remaining_water
    return result

print(solution())