def solution():
    required_cups_per_day = 2  # Federal guidelines recommend eating at least 2 cups of vegetables per day
    total_cups_eaten = 8  # Sarah has eaten 8 cups of vegetables from Sunday breakfast to Thursday end of day
    days_left = 7 - 5  # Sarah needs to eat vegetables for 7 days in a week and has already eaten for 5 days

    # Calculate the total cups required for the week
    total_cups_required = required_cups_per_day * 7

    # Calculate the remaining cups Sarah needs to eat for the week
    remaining_cups_required = total_cups_required - total_cups_eaten

    # Calculate the cups Sarah needs to eat per day to meet the daily minimum requirement for the week
    cups_per_day = remaining_cups_required / days_left
    result = cups_per_day
    return result

print(solution())