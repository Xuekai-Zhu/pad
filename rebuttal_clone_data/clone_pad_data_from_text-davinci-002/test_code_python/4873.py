def solution():
    dog_speed = 24
    rabbit_speed = 15
    head_start = 0.6
    time_to_catch = head_start / (dog_speed - rabbit_speed)
    result = time_to_catch
    return result

print(solution())