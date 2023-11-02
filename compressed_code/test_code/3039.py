def solution():
    
    jug_size = 2  
    fill_percentage = 0.7
    sand_density = 5  

    
    sand_volume = jug_size * fill_percentage
    
    sand_weight = sand_volume * sand_density
    
    total_weight = 2 * sand_weight

    result = total_weight
    return result

print(solution())