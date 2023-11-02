def solution():
    sand_density = 5
    jug_capacity = 2
    percent_full = 70
    amount_of_sand = jug_capacity * (percent_full / 100)
    sand_weight = amount_of_sand * sand_density
    weight_of_weights = sand_weight * 2
    result = weight_of_weights
    
    return result

print(solution())