def solution():
    
    fold_time = 4 * 5
    rest_time = 4 * 75
    mix_time = 10
    bake_time = 30
    total_time = fold_time + rest_time + mix_time + bake_time
    result = total_time / 60
    return result

print(solution())