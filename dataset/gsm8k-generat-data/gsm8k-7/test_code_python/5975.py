def solution():
    dog_food_weight = 1/4 # in pounds
    num_dogs = 2
    servings_per_day = 2 * 6 # 2 servings of 6 cups each
    days_per_month = 30
    total_servings = servings_per_day * days_per_month * num_dogs
    total_weight = total_servings * dog_food_weight
    bags_needed = total_weight / 20 # 1 bag holds 20 pounds of dog food
    result = bags_needed
    return result

print(solution())