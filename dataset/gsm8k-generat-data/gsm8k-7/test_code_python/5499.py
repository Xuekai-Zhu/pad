def solution():
    motorboat_speed_1 = 25
    motorboat_time_1 = 1
    motorboat_distance_1 = motorboat_speed_1 * motorboat_time_1

    motorboat_speed_2 = 20
    motorboat_time_2 = 0.5
    motorboat_distance_2 = motorboat_speed_2 * motorboat_time_2

    total_motorboat_distance = motorboat_distance_1 + motorboat_distance_2

    rowboat_speed = 10
    rowboat_time = 3
    rowboat_distance = rowboat_speed * rowboat_time

    distance_difference = total_motorboat_distance - rowboat_distance
    result = distance_difference
    return result

print(solution())