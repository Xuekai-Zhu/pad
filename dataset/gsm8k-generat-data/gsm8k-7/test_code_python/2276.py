def solution():
    juice_quarts = 6
    reduced_volume_ratio = 1/12
    sugar_cups = 1
    cups_per_quart = 4

    # Calculate the total reduced volume of the juice in quarts
    reduced_volume_quarts = juice_quarts * reduced_volume_ratio

    # Convert the reduced volume to cups
    reduced_volume_cups = reduced_volume_quarts * cups_per_quart

    # Add the volume of sugar to the reduced juice volume
    final_volume_cups = reduced_volume_cups + sugar_cups
    result = final_volume_cups
    return result

print(solution())