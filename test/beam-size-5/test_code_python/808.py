def solution():
    
    initial_flowers = 3
    initial_flowers_5 = 5
    initial_flowers_6 = 4
    initial_flowers_4 = 6
    initial_flowers_7 = 7
    total_flowers = initial_flowers + initial_flowers_6 + initial_flowers_4 + initial_flowers_7
    flowers_dropped = 6
    flowers_left = total_flowers - flowers_dropped
    result = flowers_left
    return result

print(solution())