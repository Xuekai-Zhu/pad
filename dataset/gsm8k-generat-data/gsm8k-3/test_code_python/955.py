def solution():
    """Mr. Williams bought 10 gallons of juice for a party. Each gallon has 10 cups. At the party, 5 cups of juice were left. How many cups of juice were drunk?"""
    # Define the number of gallons and cups per gallon
    GALLONS = 10
    CUPS_PER_GALLON = 10

    # Calculate the total number of cups of juice
    total_cups = GALLONS * CUPS_PER_GALLON

    # Calculate the number of cups of juice drunk
    cups_drunk = total_cups - 5

    # Display the number of cups of juice drunk
    result = cups_drunk
    return result

print(solution())