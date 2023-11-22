def solution():
    
    # Define the number of packages of cat food and dog food
    cat_food_packages = 8
    dog_food_packages = 6

    # Define the number of tins in each package of cat food and dog food
    cat_food_tins = 11
    dog_food_tins = 6

    # Calculate the total number of tins of cat food and dog food
    total_cat_food_tins = cat_food_packages * cat_food_tins
    total_dog_food_tins = dog_food_packages * dog_food_tins

    # Calculate the difference in the number of tins of cat food and dog food
    difference = total_cat_food_tins - total_dog_food_tins

    # return the result
    result = difference
    return result

print(solution())