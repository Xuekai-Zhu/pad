def solution():
    """Billy is reducing raspberry juice down to make syrup. He reduces 6 quarts of juice to 1/12 of its original volume, then adds 1 cup of sugar. What is the final volume of the syrup in cups? (There are 4 cups in a quart)"""
    original_volume = 6 * 4 # converting quarts to cups
    reduced_volume = original_volume / 12
    total_volume = reduced_volume + 1
    result = total_volume
    return result

print(solution())