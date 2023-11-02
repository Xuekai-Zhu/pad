def solution():
    
    area_A = 25
    area_B = 81
    side_length_A = round(area_A**0.5, 2)
    side_length_B = round(area_B**0.5, 2)
    length_difference = abs(side_length_B - side_length_A)
    result = length_difference
    return result

print(solution())