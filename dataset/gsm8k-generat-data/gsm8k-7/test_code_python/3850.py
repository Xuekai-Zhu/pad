def solution():
    pyramid_height = 4
    
    # Calculate the total number of cases needed for the bottom level of the pyramid
    bottom_level_side = pyramid_height
    bottom_level_area = bottom_level_side**2
    bottom_level_cases = bottom_level_area

    # Calculate the total number of cases needed for all levels of the pyramid
    total_cases = 0
    for i in range(pyramid_height):
        level_side = bottom_level_side - i
        level_area = level_side ** 2
        level_cases = level_area - total_cases
        total_cases += level_cases
        
    result = total_cases
    return result

print(solution())