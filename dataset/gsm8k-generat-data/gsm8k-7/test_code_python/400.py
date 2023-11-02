def solution():
    water_weight = 20
    food_weight = 10
    gear_weight = 20
    hours = 6
    
    # Calculate the weight of water consumed during hike
    water_consumed = 2 * hours
    
    # Calculate the weight of food consumed during hike
    food_consumed = (1/3) * water_consumed
    
    # Calculate the total weight of all items after the hike
    total_weight = water_weight - water_consumed + food_weight - food_consumed + gear_weight
    
    result = total_weight
    return result

print(solution())