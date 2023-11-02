def solution():
    
    jug_size = 2
    fill_percentage = 0.7
    sand_density = 5
    fill_amount = jug_size * fill_percentage
    weight = fill_amount * sand_density * 2
    result = weight
    
    return result

print(solution())