def solution():
    
    heavy_wash_gallons = 20
    regular_wash_gallons = 10
    light_wash_gallons = 2
    bleached_loads = 2
    
    total_gallons = (heavy_wash_gallons * 2) + (regular_wash_gallons * 3) + (light_wash_gallons * 1) + \
                    (light_wash_gallons * bleached_loads)
    
    result = total_gallons
    return result

print(solution())