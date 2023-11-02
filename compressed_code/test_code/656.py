def solution():
    
    ingredients_time = 1
    normal_bake_time = 1.5
    sprinkle_time = 1
    failed_bake_time = 2 * normal_bake_time
    total_time = ingredients_time + failed_bake_time + sprinkle_time
    result = total_time
    return result

print(solution())