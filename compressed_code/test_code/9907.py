def solution():
    
    checkered_shirts = 7
    horizontal_stripes = checkered_shirts * 4
    total_people = 40
    vertical_stripes = total_people - checkered_shirts - horizontal_stripes
    result = vertical_stripes
    return result

print(solution())