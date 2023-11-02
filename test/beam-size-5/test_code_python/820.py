def solution():
    num_cat_food_packages = 8
    cat_food_tins_per_package = 11

    num_dog_food_packages = 6
    dog_food_tins_per_package = 6

    # Calculate the total number of tins of cat food
    total_cat_food_tins = num_cat_food_packages * cat_food_tins_per_package

    # Calculate the total number of tins of dog food
    total_dog_food_tins = num_dog_food_packages * dog_food_tins_per_package

    # Calculate the difference between the number of tins of cat food and dog food
    difference = total_cat_food_tins - total_dog_food_tins
    result = difference
    return result

print(solution())