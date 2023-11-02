def solution():
    # Define the initial weights
    water_weight = 20
    food_weight = 10
    gear_weight = 20
    
    # Calculate the weight of water and food consumed during the hike
    water_consumed = 2 * 6 # 2 pounds consumed per hour for 6 hours
    food_consumed = (1/3) * water_consumed # 1/3rd the weight of water per hour
    
    # Subtract the weight of consumed water and food from their initial weights
    water_weight -= water_consumed
    food_weight -= food_consumed
    
    # Calculate the total weight after 6 hours
    total_weight = water_weight + food_weight + gear_weight
    result = total_weight
    return result

print(solution())