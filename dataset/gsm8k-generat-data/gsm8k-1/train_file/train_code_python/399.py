def solution():
    """Karen is packing her backpack for a long-distance hike. She packs 20 pounds of water, 10 pounds of food, and 20 pounds of gear. During her hike, she drinks 2 pounds of water per hour and eats 1/3rd the weight of food per hour as water per hour. How much weight is she carrying after six hours?"""
    water_weight = 20
    food_weight = 10
    gear_weight = 20
    total_weight = water_weight + food_weight + gear_weight
    water_consumed = 2 * 6  # 2 pounds per hour for 6 hours
    food_consumed = (2/3) * water_consumed  # 1/3 the weight of food per hour as water per hour
    total_consumed_weight = water_consumed + food_consumed
    weight_after_six_hours = total_weight - total_consumed_weight
    
    result = weight_after_six_hours
    return result

print(solution())