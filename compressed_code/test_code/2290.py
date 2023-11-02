def solution():
    
    bottom_level = 7
    second_level = bottom_level - 1
    third_level = second_level - 1
    total_legos = bottom_level**2 + second_level**2 + third_level**2
    result = total_legos
    return result

print(solution())