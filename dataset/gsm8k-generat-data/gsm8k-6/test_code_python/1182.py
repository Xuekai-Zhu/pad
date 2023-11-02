def solution():
    # Calculate the total weight of cat food
    cat_food_weight = 3 * 2  # 2 bags of 3-pound cat food

    # Calculate the weight of one bag of dog food
    dog_food_weight = 3 + 2  # each bag of dog food weighs 2 more pounds than each bag of cat food

    # Calculate the total weight of dog food
    total_dog_food_weight = 2 * dog_food_weight  # 2 bags of dog food

    # Calculate the total weight of pet food in pounds
    total_weight = cat_food_weight + total_dog_food_weight

    # Convert the total weight of pet food to ounces
    total_weight_ounces = total_weight * 16

    result = total_weight_ounces
    return result

print(solution())