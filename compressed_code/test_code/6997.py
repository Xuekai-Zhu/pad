def solution():
    
    current_bunches = 8
    current_flowers_per_bunch = 9
    new_flowers_per_bunch = 12
    new_bunches = (current_bunches * current_flowers_per_bunch) / new_flowers_per_bunch
    result = new_bunches
    return result

print(solution())