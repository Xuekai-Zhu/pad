def solution():
    base_speed = 30
    speed_decrease = 50
    speed_increase = 20
    distance_to_top = 60
    distance_to_bottom = 72
    time_to_top = distance_to_top / base_speed
    reduced_speed = base_speed - (base_speed * (speed_decrease / 100))
    time_to_bottom = distance_to_bottom / reduced_speed
    total_time = time_to_top + time_to_bottom
    result = total_time
    return result

print(solution())