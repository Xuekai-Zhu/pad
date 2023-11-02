def solution():
    # Define the weight of each bag of cat food
    cat_weight = 3

    # Define the weight of each bag of dog food
    dog_weight = cat_weight + 2

    # Calculate the total weight of the cat food
    total_cat_weight = 2 * cat_weight

    # Calculate the total weight of the dog food
    total_dog_weight = 2 * dog_weight

    # Calculate the total weight in ounces
    total_weight_ounces = (total_cat_weight + total_dog_weight) * 16

    result = total_weight_ounces
    return result

print(solution())