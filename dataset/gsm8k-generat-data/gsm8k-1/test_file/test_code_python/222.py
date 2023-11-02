def solution():
    """James is counting his Pokemon cards. He has 30 fire type, 20 grass type, and 40 water type. If he loses 8 of the water type and buys 14 grass type, what's the percentage chance (rounded to the nearest integer) that a randomly picked card will be a water type?"""
    fire_type = 30
    original_grass_type = 20
    water_type = 40
    lost_water_type = 8
    new_grass_type = 14
    
    # Calculate the new number of water and grass types
    new_water_type = water_type - lost_water_type
    new_total_cards = fire_type + new_grass_type + new_water_type
    
    # Calculate the percentage chance of picking a water type card
    water_type_chance = (new_water_type / new_total_cards) * 100
    result = round(water_type_chance)
    return result

print(solution())