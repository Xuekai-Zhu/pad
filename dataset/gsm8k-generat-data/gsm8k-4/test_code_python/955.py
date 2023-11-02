def solution():
    """Mr. Williams bought 10 gallons of juice for a party. Each gallon has 10 cups. At the party, 5 cups of juice were left. How many cups of juice were drunk?"""
    # Define the number of gallons and cups per gallon
    gallons = 10
    cups_per_gallon = 10

    # Calculate the total number of cups
    total_cups = gallons * cups_per_gallon

    # Calculate the number of cups left
    cups_left = 5

    # Calculate the number of cups drunk
    cups_drunk = total_cups - cups_left

    # return the result
    result = cups_drunk
    return result

print(solution())