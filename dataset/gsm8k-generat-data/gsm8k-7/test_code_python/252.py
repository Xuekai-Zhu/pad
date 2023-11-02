def solution():
    num_pounds = 3
    cups_per_pound = 40
    cups_per_day = 3

    # Calculate the total number of cups of coffee in the coffee purchased
    total_cups = num_pounds * cups_per_pound

    # Calculate the number of days this coffee will last Angie
    num_days = total_cups / cups_per_day
    result = num_days
    return result

print(solution())