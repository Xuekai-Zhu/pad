def solution():
    """Blake wants to spend his Friday making milkshakes for his family. He knows that he needs 4 ounces of milk and 12 ounces of ice cream for each milkshake. If he has 72 ounces of milk and 192 ounces of ice cream, how much milk will be left over when he is done?"""
    # Determine how many milkshakes Blake can make with the available ingredients
    milkshakes = min(72/4, 192/12)

    # Calculate how much milk is needed for the milkshakes
    milk_needed = milkshakes * 4

    # Calculate how much milk is left over
    milk_left = 72 - milk_needed

    # Display how much milk is left over
    result = milk_left
    return result

print(solution())