def solution():
    width = 110
    length = 120
    tiller_width = 2
    tilling_speed = 1/2
    total_area = width * length
    tilling_time = total_area * tilling_speed
    tilling_time_in_minutes = tilling_time / 60
    result = tilling_time_in_minutes
    return result

print(solution())