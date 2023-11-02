def solution():
    
    jar_size_liters = 2
    num_jars = 5
    glass_size_ml = 250
    total_juice_ml = jar_size_liters * 1000 * num_jars
    total_glasses = total_juice_ml // glass_size_ml
    result = total_glasses
    return result

print(solution())