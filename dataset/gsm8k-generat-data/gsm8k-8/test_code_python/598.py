def solution():
    # Calculate the remaining cups she needs to eat for the week
    remaining_cups = 2 * 7 - 8

    # Calculate how many days are left in the week
    days_left = 7 - 4

    # Calculate how many cups she needs to eat per day
    cups_per_day = remaining_cups / days_left
    result = cups_per_day
    return result

print(solution())