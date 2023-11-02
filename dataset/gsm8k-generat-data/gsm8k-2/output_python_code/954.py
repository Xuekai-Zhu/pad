def solution():
    """Mr. Williams bought 10 gallons of juice for a party. Each gallon has 10 cups. At the party, 5 cups of juice were left. How many cups of juice were drunk?"""
    total_cups = 10 * 10
    cups_left = 5
    cups_drunk = total_cups - cups_left
    result = cups_drunk
    return result

print(solution())