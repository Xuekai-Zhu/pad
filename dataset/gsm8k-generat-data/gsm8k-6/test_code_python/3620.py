def solution():
    # Calculate the volume of water already in the tank
    current_volume = (1/3) * tank_volume

    # Calculate the final volume of water after filling the tank
    final_volume = current_volume + 16

    # Calculate the total volume of the tank
    tank_volume = final_volume / (2/3)
    result = tank_volume
    return result

print(solution())