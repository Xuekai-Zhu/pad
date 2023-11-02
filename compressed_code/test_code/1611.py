def solution():
    
    hallway_length = 16
    father_speed = 3
    son_speed = 1
    ratio = father_speed / (father_speed + son_speed)
    distance_from_father_end = ratio * hallway_length
    result = distance_from_father_end
    return result

print(solution())