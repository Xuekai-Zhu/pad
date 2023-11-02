def solution():
    
    sheep_speed = 12
    dog_speed = 20
    distance = 160
    relative_speed = dog_speed - sheep_speed
    time_to_catch = distance / relative_speed
    result = time_to_catch
    return result

print(solution())