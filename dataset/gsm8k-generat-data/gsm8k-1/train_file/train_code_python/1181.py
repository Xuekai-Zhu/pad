def solution():
    """Mrs. Anderson bought 2 bags of 3-pound bag of cat food and another 2 bags of dog food that each weigh 2 more pounds than each bag of cat food. There are 16 ounces in each pound. How many ounces of pet food did Mrs. Anderson buy?"""
    cat_food_weight = 3
    dog_food_weight = cat_food_weight + 2
    total_cats = 2
    total_dogs = 2
    total_cat_food = cat_food_weight * total_cats
    total_dog_food = dog_food_weight * total_dogs
    total_weight_pounds = total_cat_food + total_dog_food
    total_weight_ounces = total_weight_pounds * 16
    result = total_weight_ounces
    return result

print(solution())