def solution():
    cups_per_dog_per_meal = 1.5
    num_dogs = 2
    meals_per_day = 3
    cups_per_pound = 2.25

    # Calculate the total number of cups of food consumed per day
    total_cups_per_day = cups_per_dog_per_meal * num_dogs * meals_per_day

    # Calculate the total number of pounds of food consumed per day
    total_pounds_per_day = total_cups_per_day / cups_per_pound

    result = total_pounds_per_day
    return result

print(solution())