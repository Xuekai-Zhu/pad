def solution():
    total_distance = 24
    total_time = 8
    initial_speed = 4
    initial_time = 4
    final_distance = total_distance - (initial_speed * initial_time)
    final_time = total_time - initial_time
    final_speed = final_distance / final_time
    result = final_speed
    return result

print(solution())