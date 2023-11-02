def solution():
    
    black_capacity = 4000
    blue_capacity = black_capacity * 2
    red_capacity = blue_capacity * 3
    total_capacity = (3 * red_capacity) + (4 * blue_capacity) + (7 * black_capacity)
    result = total_capacity
    return result

print(solution())