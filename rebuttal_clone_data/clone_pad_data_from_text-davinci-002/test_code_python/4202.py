def solution():
    total_time = 2
    baking_time = 15
    cooling_time_one = 30
    cooling_time_two = 30
    total_cooling_time = cooling_time_one + cooling_time_two
    dough_time = total_time - baking_time - total_cooling_time
    result = dough_time
    return result

print(solution())