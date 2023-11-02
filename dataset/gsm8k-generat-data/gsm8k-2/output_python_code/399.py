def solution():
    """Karen is packing her backpack for a long-distance hike. She packs 20 pounds of water, 10 pounds of food, and 20 pounds of gear. During her hike, she drinks 2 pounds of water per hour and eats 1/3rd the weight of food per hour as water per hour. How much weight is she carrying after six hours?"""
    water_weight = 20
    food_weight = 10
    gear_weight = 20
    total_weight = water_weight + food_weight + gear_weight
    water_consumption = 2 * 6
    food_consumption = (1/3) * water_consumption
    total_consumption = water_consumption + food_consumption
    final_weight = total_weight - total_consumption
    result = final_weight
    return result

print(solution())