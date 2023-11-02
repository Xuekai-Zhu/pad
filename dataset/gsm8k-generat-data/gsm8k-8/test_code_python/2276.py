def solution():
    # Calculate the final volume of the juice in quarts
    final_volume = 6 * (1/12)

    # Convert the final volume to cups
    final_volume_cups = final_volume * 4

    # Add the volume of the sugar
    final_volume_cups += 1

    result = final_volume_cups
    return result

print(solution())