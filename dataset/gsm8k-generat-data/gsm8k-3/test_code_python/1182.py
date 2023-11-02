def solution():
    """Mrs. Anderson bought 2 bags of 3-pound bag of cat food and another 2 bags of dog food that each weigh 2 more pounds than each bag of cat food. There are 16 ounces in each pound. How many ounces of pet food did Mrs. Anderson buy?"""
    # Define the weight of each bag of cat food and dog food
    CAT_BAG_WEIGHT = 3
    DOG_BAG_WEIGHT = CAT_BAG_WEIGHT + 2

    # Define the number of bags of each type of pet food purchased
    cat_bags = 2
    dog_bags = 2

    # Convert the bag weights from pounds to ounces
    cat_bag_weight_oz = CAT_BAG_WEIGHT * 16
    dog_bag_weight_oz = DOG_BAG_WEIGHT * 16

    # Calculate the total weight of the pet food in ounces
    total_weight_oz = (cat_bags * cat_bag_weight_oz) + (dog_bags * dog_bag_weight_oz)

    # Display the total weight of the pet food in ounces
    result = total_weight_oz
    return result

print(solution())