def solution():
    """Karen is packing her backpack for a long-distance hike. She packs 20 pounds of water, 10 pounds of food, and 20 pounds of gear. During her hike, she drinks 2 pounds of water per hour and eats 1/3rd the weight of food per hour as water per hour. How much weight is she carrying after six hours?"""
    # Define the initial weight of the backpack
    backpack_weight = 50

    # Define the weight of water and food
    water_weight = 20
    food_weight = 10

    # Define the weight of gear
    gear_weight = 20

    # Calculate the weight of water and food consumed after 6 hours
    water_consumed = 2 * 6
    food_consumed = (2/3) * water_consumed

    # Calculate the total weight of the backpack after 6 hours
    backpack_weight = backpack_weight - water_consumed - food_consumed + gear_weight

    # return the result
    result = backpack_weight
    return result

print(solution())