def solution():
    cat_food_weight = 3  # Each bag of cat food weighs 3 pounds
    dog_food_weight = cat_food_weight + 2  # Each bag of dog food weighs 2 pounds more than each bag of cat food
    bags_of_cat_food = 2  # Mrs. Anderson bought 2 bags of cat food
    bags_of_dog_food = 2  # Mrs. Anderson bought 2 bags of dog food

    # Calculate the total weight of the cat food
    total_cat_food_weight = cat_food_weight * bags_of_cat_food

    # Calculate the total weight of the dog food
    total_dog_food_weight = dog_food_weight * bags_of_dog_food

    # Calculate the total weight of all the pet food in pounds
    total_weight_pounds = total_cat_food_weight + total_dog_food_weight

    # Convert the total weight of all the pet food to ounces
    total_weight_ounces = total_weight_pounds * 16

    result = total_weight_ounces
    return result

print(solution())