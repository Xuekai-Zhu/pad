def solution():
    food_dog_eats = 4
    food_ella_eats = 1
    days = 10
    food_ella_eats_per_day = 20
    total_food_ella_eats = food_ella_eats_per_day * days
    total_food_dog_eats = food_dog_eats * total_food_ella_eats
    total_food = total_food_ella_eats + total_food_dog_eats
    result = total_food
    return result

print(solution())