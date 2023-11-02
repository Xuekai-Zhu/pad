def solution():
    
    resistance_time = 20
    distance = 64
    rate = 8
    walking_time = distance / rate
    total_time = resistance_time + walking_time
    result = total_time
    return result

print(solution())