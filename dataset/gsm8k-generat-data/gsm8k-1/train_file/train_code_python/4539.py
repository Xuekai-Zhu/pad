def solution():
    """Tracy feeds each of her two dogs 1.5 cups of food per meal. She feeds her dogs thrice a day. How many pounds of food do her two dogs consume if 1 pound is equal to 2.25 cups?"""
    cups_per_dog_per_meal = 1.5
    number_of_dogs = 2
    meals_per_day = 3
    cups_per_day = cups_per_dog_per_meal * number_of_dogs * meals_per_day
    cups_per_pound = 2.25
    pounds_per_day = cups_per_day / cups_per_pound
    result = pounds_per_day
    return result

print(solution())