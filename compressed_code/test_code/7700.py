def solution():
    
    total_fluid_ounces = 64
    old_serving_size = 8
    new_serving_size = 16
    old_servings = total_fluid_ounces / old_serving_size
    new_servings = total_fluid_ounces / new_serving_size
    fewer_servings = old_servings - new_servings
    result = fewer_servings
    return result

print(solution())