def solution():
    
    cups_per_dog_per_meal = 1.5
    number_of_dogs = 2
    meals_per_day = 3
    cups_per_day = cups_per_dog_per_meal * number_of_dogs * meals_per_day
    cups_per_pound = 2.25
    pounds_per_day = cups_per_day / cups_per_pound
    result = pounds_per_day
    return result

print(solution())