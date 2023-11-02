def solution():
    
    file_size = 90
    first_slow_part = 60
    first_slow_speed = 5
    second_fast_speed = 10
    time_first_slow = first_slow_part / first_slow_speed
    time_second_fast = (file_size - first_slow_part) / second_fast_speed
    total_time = time_first_slow + time_second_fast
    result = total_time
    return result

print(solution())