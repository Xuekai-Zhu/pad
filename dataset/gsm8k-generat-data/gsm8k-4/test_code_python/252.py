def solution():
    """Angie bought 3 lbs. of coffee at the store today. Each lb. of coffee will brew about 40 cups of coffee. Angie drinks 3 cups of coffee every day. How many days will this coffee last her?"""
    # Define the amount of coffee and cups per pound
    COFFEE_PER_POUND = 40
    CUPS_PER_DAY = 3

    # Define the total amount of coffee
    total_coffee = 3

    # Calculate the total number of cups of coffee
    total_cups = total_coffee * COFFEE_PER_POUND

    # Calculate the number of days the coffee will last
    days = total_cups // CUPS_PER_DAY

    result = days
    return result

print(solution())