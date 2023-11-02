def solution():
    times_around_block = 4
    meters_per_block = 200
    mickey_times_around = times_around_block / 2
    mickey_distance = mickey_times_around * meters_per_block
    johnny_distance = times_around_block * meters_per_block
    average_distance = (mickey_distance + johnny_distance) / 2
    result = average_distance
    return result

print(solution())