def solution():
    
    cat_food_weight = 3
    dog_food_weight = cat_food_weight + 2
    total_cats = 2
    total_dogs = 2
    total_cat_food = cat_food_weight * total_cats
    total_dog_food = dog_food_weight * total_dogs
    total_weight_pounds = total_cat_food + total_dog_food
    total_weight_ounces = total_weight_pounds * 16
    result = total_weight_ounces
    return result

print(solution())