def solution():
    # Calculate the total number of meals the chef has for dinner
    remaining_meals = 17 - 12  # subtract the number of meals sold during lunch from the number of meals prepared
    total_meals = remaining_meals + 5  # add the number of meals prepared for dinner to the remaining meals
    result = total_meals
    return result

print(solution())