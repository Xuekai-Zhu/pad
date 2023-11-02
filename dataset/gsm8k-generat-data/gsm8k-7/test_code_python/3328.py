def solution():
    num_dogs = 3
    total_food_per_week = 15 * num_dogs
    second_dog_food_per_week = 13 * 2
    third_dog_food_per_week = total_food_per_week - second_dog_food_per_week - 13
    result = third_dog_food_per_week
    return result

print(solution())