def solution():
    tank_capacity = 8000
    initial_volume = tank_capacity * 3/4

    # Calculate the volume of water emptied from the tank
    emptied_volume = initial_volume * 40/100

    # Calculate the remaining volume of water in the tank
    remaining_volume = initial_volume - emptied_volume

    # Calculate the volume of water filled back into the tank
    filled_volume = remaining_volume * 30/100

    # Calculate the final volume of water in the tank
    final_volume = remaining_volume + filled_volume
    result = final_volume
    return result

print(solution())