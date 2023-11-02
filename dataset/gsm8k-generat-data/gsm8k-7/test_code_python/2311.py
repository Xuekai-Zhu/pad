def solution():
    num_dogs = 3
    food_per_dog = 0.5  # in pounds
    num_feedings_per_day = 2
    num_days = 7

    total_food_consumed = num_dogs * food_per_dog * num_feedings_per_day * num_days

    food_left = 30 - total_food_consumed
    result = food_left
    return result

print(solution())