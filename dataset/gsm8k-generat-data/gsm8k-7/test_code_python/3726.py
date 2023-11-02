def solution():
    num_cat_food_packages = 6
    num_cat_food_cans_per_package = 9

    num_dog_food_packages = 2
    num_dog_food_cans_per_package = 3

    # Calculate the total number of cans of cat food
    total_cat_food_cans = num_cat_food_packages * num_cat_food_cans_per_package

    # Calculate the total number of cans of dog food
    total_dog_food_cans = num_dog_food_packages * num_dog_food_cans_per_package

    # Calculate the difference between the total number of cans of cat food and dog food
    num_more_cat_food_cans = total_cat_food_cans - total_dog_food_cans
    result = num_more_cat_food_cans
    return result

print(solution())