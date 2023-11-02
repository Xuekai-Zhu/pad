def solution():
    
    bottom_level = 7
    middle_level = bottom_level - 1
    top_level = middle_level - 1
    total_legos = bottom_level**2 + middle_level**2 + top_level**2
    result = total_legos
    return result

print(solution())