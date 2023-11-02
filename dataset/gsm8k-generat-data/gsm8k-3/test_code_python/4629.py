def solution():
    """Josette bought 3 bottles of mineral water for €1.50. How much will four bottles cost?"""
    # Define the cost of three bottles of mineral water
    cost_3_bottles = 1.5

    # Calculate the cost of one bottle of mineral water
    cost_1_bottle = cost_3_bottles / 3

    # Calculate the cost of four bottles of mineral water
    cost_4_bottles = cost_1_bottle * 4

    # Display the cost of four bottles of mineral water
    result = cost_4_bottles
    return result

print(solution())