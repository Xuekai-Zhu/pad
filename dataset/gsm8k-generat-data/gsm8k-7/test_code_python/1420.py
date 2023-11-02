def solution():
    total_drinks = 54
    soda_ratio = 3
    soda_offset = 6
    
    # Calculate the total amount of soda Carla drank
    total_soda = (total_drinks / (soda_ratio+1)) * soda_ratio
    
    # Calculate the total amount of water Carla drank
    total_water = total_drinks - (total_soda - soda_offset)
    result = total_water
    return result

print(solution())