def solution():
    
    checkered_shirts = 7
    horizontal_stripes = 4 * checkered_shirts
    total_checked_horizontal = checkered_shirts + horizontal_stripes
    vertical_stripes = 40 - total_checked_horizontal
    result = vertical_stripes
    return result

print(solution())