def solution():
    
    length = 10
    width = 8
    depth = 6
    water_volume = length * width * depth
    chlorine_volume = water_volume / 120
    chlorine_cost = 3
    total_cost = chlorine_volume * chlorine_cost
    result = total_cost
    return result

print(solution())