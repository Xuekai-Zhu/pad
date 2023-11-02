def solution():
    
    total_people = 100
    blue_eyes = 19
    brown_eyes = total_people / 2
    black_eyes = total_people / 4
    green_eyes = total_people - blue_eyes - brown_eyes - black_eyes
    result = green_eyes
    return result

print(solution())