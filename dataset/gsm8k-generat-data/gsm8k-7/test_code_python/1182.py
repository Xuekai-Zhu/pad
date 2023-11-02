def solution():
    cat_food_weight = 3  # pounds
    dog_food_weight = cat_food_weight + 2  # pounds
    ounces_per_pound = 16

    # Calculate the total weight of cat food in pounds and ounces
    total_cat_food_weight = cat_food_weight * 2  # 2 bags of cat food
    total_cat_food_weight_oz = total_cat_food_weight * ounces_per_pound

    # Calculate the total weight of dog food in pounds and ounces
    total_dog_food_weight = dog_food_weight * 2  # 2 bags of dog food
    total_dog_food_weight_oz = total_dog_food_weight * ounces_per_pound

    # Calculate the total weight of all pet food in ounces
    total_weight_oz = total_cat_food_weight_oz + total_dog_food_weight_oz
    result = total_weight_oz
    return result

print(solution())