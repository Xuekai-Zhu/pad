def solution():
    # Calculate the final volume of syrup in cups
    reduced_volume_quarts = 6 * (1/12)  # the juice is reduced to 1/12 of its original volume
    reduced_volume_cups = reduced_volume_quarts * 4  # converting quarts to cups
    final_volume_cups = reduced_volume_cups + 1  # adding 1 cup of sugar
    result = final_volume_cups
    return result

print(solution())