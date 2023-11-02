def solution():
    initial_distance = 270
    initial_time = 3
    rate = initial_distance / initial_time
    additional_distance = 180
    additional_time = additional_distance / rate
    result = additional_time
    return result

print(solution())