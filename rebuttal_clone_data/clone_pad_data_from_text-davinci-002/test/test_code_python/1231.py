def solution():
    initial_speed = 80
    initial_time = 6
    second_speed = 60
    second_time = 4
    final_speed = 40
    final_time = 2
    initial_distance = initial_speed * initial_time
    second_distance = second_speed * second_time
    final_distance = final_speed * final_time
    total_distance = initial_distance + second_distance + final_distance
    result = total_distance
    return result

print(solution())