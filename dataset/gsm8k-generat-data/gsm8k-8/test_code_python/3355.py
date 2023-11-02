def solution():
    # Define the tank capacity and initial fill level
    tank_capacity = 8000
    initial_fill = tank_capacity * 3/4

    # Calculate the amount of water Daxton removes
    removed_water = initial_fill * 0.4

    # Calculate the amount of water remaining in the tank
    remaining_water = initial_fill - removed_water

    # Calculate the amount of water Daxton adds back
    added_water = remaining_water * 0.3

    # Calculate the final volume of water in the tank
    final_volume = remaining_water + added_water
    result = final_volume
    return result

print(solution())