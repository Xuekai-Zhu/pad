def solution():
    # Calculate the total amount of food the puppy will eat in the first two weeks
    num_meals_per_day_1 = 3
    num_days_1 = 14
    serving_size_1 = 0.25
    total_servings_1 = num_meals_per_day_1 * num_days_1 * serving_size_1

    # Calculate the total amount of food the puppy will eat in the next two weeks
    num_meals_per_day_2 = 2
    num_days_2 = 14
    serving_size_2 = 0.5
    total_servings_2 = num_meals_per_day_2 * num_days_2 * serving_size_2

    # Calculate the total amount of food the puppy has already eaten
    servings_today = 0.5

    # Calculate the total amount of food the puppy will eat over the next four weeks
    total_servings = total_servings_1 + total_servings_2 + servings_today
    result = total_servings
    return result

print(solution())