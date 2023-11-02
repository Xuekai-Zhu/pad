def solution():
    """Mrs. Anderson bought 2 bags of 3-pound bag of cat food and another 2 bags of dog food that each weigh 2 more pounds than each bag of cat food. There are 16 ounces in each pound. How many ounces of pet food did Mrs. Anderson buy?"""
    # Define the weight of each bag of cat food and dog food in pounds
    cat_food_weight = 3
    dog_food_weight = cat_food_weight + 2

    # Define the number of bags of each type of food bought
    cat_food_bags = 2
    dog_food_bags = 2

    # Calculate the total weight of cat food in ounces
    total_cat_food_weight = cat_food_weight * cat_food_bags * 16

    # Calculate the total weight of dog food in ounces
    total_dog_food_weight = dog_food_weight * dog_food_bags * 16

    # Calculate the total weight of pet food in ounces
    total_pet_food_weight = total_cat_food_weight + total_dog_food_weight

    result = total_pet_food_weight
    return result

print(solution())