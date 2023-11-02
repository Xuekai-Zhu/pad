def solution():
    
    building_height = 96
    bounce_height = building_height
    for i in range(5):
        bounce_height /= 2
    result = bounce_height
    return result

print(solution())