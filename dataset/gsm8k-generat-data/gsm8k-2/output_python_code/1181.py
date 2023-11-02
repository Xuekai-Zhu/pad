def solution():
    """Mrs. Anderson bought 2 bags of 3-pound bag of cat food and another 2 bags of dog food that each weigh 2 more pounds than each bag of cat food. There are 16 ounces in each pound. How many ounces of pet food did Mrs. Anderson buy?"""

    cat_food_weight = 3
    dog_food_weight = cat_food_weight + 2
    total_cat_food_weight = cat_food_weight * 2
    total_dog_food_weight = dog_food_weight * 2
    total_weight = total_cat_food_weight + total_dog_food_weight
    ounces_per_pound = 16
    total_ounces = total_weight * ounces_per_pound

    result = total_ounces
    return result

print(solution())