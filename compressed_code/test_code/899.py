def solution():
    

    cat_food_weight = 3
    dog_food_weight = cat_food_weight + 2
    total_cat_food_weight = cat_food_weight * 2
    total_dog_food_weight = dog_food_weight * 2
    total_weight = total_cat_food_weight + total_dog_food_weight
    ounces_per_pound = 16
    total_ounces = total_weight * ounces_per_pound

    result = total_ounces
    return result

print(solution())