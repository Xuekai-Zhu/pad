def solution():
    
    rise_time = 3
    bake_time = 2
    total_time = 0
    for i in range(4):
        total_time += rise_time + bake_time
    result = total_time
    return result

print(solution())