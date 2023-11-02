def solution():
    num_family_members = 5  # Tom + parents + siblings
    num_meals_per_day = 3
    num_days = 4
    plates_per_meal = 2

    # Calculate the total number of meals for Tom and his guests
    total_meals = num_family_members * num_meals_per_day * num_days

    # Calculate the total number of plates used for all the meals
    total_plates_used = total_meals * plates_per_meal
    result = total_plates_used
    return result

print(solution())