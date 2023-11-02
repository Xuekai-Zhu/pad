def solution():
    """Chad bought 6 packages of cat food and 2 packages of dog food. Each package of cat food contained 9 cans, and each package of dog food contained 3 cans. How many more cans of cat food than dog food did Chad buy?"""
    cat_food_packages = 6
    dog_food_packages = 2
    cans_per_cat_food_package = 9
    cans_per_dog_food_package = 3
    total_cat_cans = cat_food_packages * cans_per_cat_food_package
    total_dog_cans = dog_food_packages * cans_per_dog_food_package
    difference = total_cat_cans - total_dog_cans
    
    return difference

print(solution())