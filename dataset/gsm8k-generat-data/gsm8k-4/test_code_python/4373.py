def solution():
    """Lucille made an agreement with her mom that she would earn six cents for every weed she pulled in her mom's garden. There are eleven weeds in the flower bed, fourteen in the vegetable patch, and thirty-two in the grass around the fruit trees. Lucille weeded the flower bed, the vegetable patch, and half the grass before she took a break. She bought a soda for 99 cents on her break with some of her earnings. How many cents does Lucille have left?"""
    # Define the payment per weed and the number of weeds in each area
    PAYMENT_PER_WEED = 6
    WEEDS_FLOWER_BED = 11
    WEEDS_VEGETABLE_PATCH = 14
    WEEDS_GRASS_FRUIT_TREES = 32

    # Calculate the total number of weeds and the earnings from pulling them
    total_weeds = WEEDS_FLOWER_BED + WEEDS_VEGETABLE_PATCH + WEEDS_GRASS_FRUIT_TREES
    earnings = total_weeds * PAYMENT_PER_WEED

    # Calculate the cost of the soda she bought
    soda_cost = 99

    # Calculate the remaining amount of money she has
    remaining_money = earnings - soda_cost

    result = remaining_money
    return result

print(solution())