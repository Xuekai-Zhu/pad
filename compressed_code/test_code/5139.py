def solution():
    
    x = 1  
    largest_angle = 5 * x
    middle_angle = 3 * x
    smallest_angle = x
    total = largest_angle + middle_angle + smallest_angle
    while total != 180:  
        x += 1
        largest_angle = 5 * x
        middle_angle = 3 * x
        smallest_angle = x
        total = largest_angle + middle_angle + smallest_angle

    result = smallest_angle
    return result

print(solution())