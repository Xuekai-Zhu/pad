def solution():
    cups_per_dog_per_day = 1.5 * 3  # Each dog is fed 1.5 cups of food, thrice a day
    cups_per_day_for_two_dogs = cups_per_dog_per_day * 2  # Total cups per day for two dogs
    pounds_per_day_for_two_dogs = cups_per_day_for_two_dogs / 2.25  # Convert cups to pounds
    pounds_per_month_for_two_dogs = pounds_per_day_for_two_dogs * 30  # Assuming 30 days in a month

    result = pounds_per_month_for_two_dogs
    return result

print(solution())