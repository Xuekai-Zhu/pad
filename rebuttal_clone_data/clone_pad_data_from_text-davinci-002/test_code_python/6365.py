def solution():
    track_1_length = 200
    track_2_length = 240
    track_1_speed = 50
    track_2_speed = 80
    total_time = (track_1_length / track_1_speed) + (track_2_length / track_2_speed)
    result = round(total_time)
    return result

print(solution())