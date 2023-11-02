def solution():
    """Billy is reducing raspberry juice down to make syrup. He reduces 6 quarts of juice to 1/12 of its original volume, then adds 1 cup of sugar. What is the final volume of the syrup in cups? (There are 4 cups in a quart)"""
    juice_quarts = 6
    juice_final = juice_quarts / 12
    sugar_cups = 1
    final_volume = (juice_final * 4) + sugar_cups
    result = final_volume
    return result

print(solution())