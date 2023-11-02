def solution():
    """Angie bought 3 lbs. of coffee at the store today. Each lb. of coffee will brew about 40 cups of coffee. Angie drinks 3 cups of coffee every day. How many days will this coffee last her?"""
    # Define the number of cups of coffee per pound
    CUPS_PER_POUND = 40

    # Define the amount of coffee Angie bought
    pounds_of_coffee = 3

    # Calculate the total number of cups of coffee Angie can brew
    total_cups = pounds_of_coffee * CUPS_PER_POUND

    # Calculate the number of days the coffee will last Angie
    cups_per_day = 3
    days_of_coffee = total_cups // cups_per_day

    # Display the number of days the coffee will last Angie
    result = days_of_coffee
    return result

print(solution())