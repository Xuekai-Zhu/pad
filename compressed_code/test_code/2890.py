def solution():
    
    cat_food_packages = 6
    dog_food_packages = 2
    cans_per_cat_food_package = 9
    cans_per_dog_food_package = 3
    total_cat_food_cans = cat_food_packages * cans_per_cat_food_package
    total_dog_food_cans = dog_food_packages * cans_per_dog_food_package
    difference = total_cat_food_cans - total_dog_food_cans
    result = difference
    return result

print(solution())