def solution():
    initial_time = 1.5
    initial_speed = 60
    second_time = 2
    second_speed = 45
    total_time = initial_time + second_time
    total_distance = (initial_speed * initial_time) + (second_speed * second_time)
    result = total_distance
    return result

print(solution())