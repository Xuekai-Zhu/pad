def solution():
    """Mr. Williams bought 10 gallons of juice for a party. Each gallon has 10 cups. At the party, 5 cups of juice were left. How many cups of juice were drunk?"""
    gallons = 10
    cups_per_gallon = 10
    total_cups = gallons * cups_per_gallon
    cups_left = 5
    cups_drunk = total_cups - cups_left
    result = cups_drunk
    return result

print(solution())