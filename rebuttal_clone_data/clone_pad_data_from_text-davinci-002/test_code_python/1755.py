def solution():
    original_distance = 150
    extra_distance = 50
    total_distance = original_distance + extra_distance
    original_time = 3
    speed = total_distance / original_time
    extra_time = extra_distance / speed
    total_time = original_time + extra_time
    result = total_time
    return result

print(solution())