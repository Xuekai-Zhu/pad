def solution():
    """Tracy feeds each of her two dogs 1.5 cups of food per meal. She feeds her dogs thrice a day. How many pounds of food do her two dogs consume if 1 pound is equal to 2.25 cups?"""
    # Define the number of dogs and cups of food per meal
    DOGS = 2
    CUPS_PER_MEAL = 1.5

    # Calculate the total cups of food consumed per day
    cups_per_day = DOGS * CUPS_PER_MEAL * 3

    # Calculate the total pounds of food consumed per day
    pounds_per_day = cups_per_day / 2.25

    # Return the result
    result = pounds_per_day
    return result

print(solution())