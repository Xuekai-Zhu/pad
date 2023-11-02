def solution():
    # Calculate the weight of one steel bar
    tin_to_steel_ratio = 1/2
    steel_weight = 90 * (1 + tin_to_steel_ratio)
    
    # Calculate the weight of one copper bar
    copper_weight = 90
    
    # Calculate the total weight of 20 bars of each metal
    total_weight = 20 * (steel_weight + copper_weight)
    result = total_weight
    return result

print(solution())