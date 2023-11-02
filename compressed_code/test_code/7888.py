def solution():
    
    doughnuts_per_dozen = 12
    doughnuts_per_box = 2 * doughnuts_per_dozen
    doughnuts_eaten = 8
    doughnuts_left = doughnuts_per_box - doughnuts_eaten
    result = doughnuts_left
    return result

print(solution())