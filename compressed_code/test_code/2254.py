def solution():
    
    distance = 480
    speed = 60
    driving_time = distance / speed
    break_time = (30 + 15 + 15) / 60
    total_time = driving_time + break_time
    result = total_time
    return result

print(solution())