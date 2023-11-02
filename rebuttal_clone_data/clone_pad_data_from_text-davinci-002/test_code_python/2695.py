def solution():
    time_ bathing = 20
    time_blowdrying = time_bathing / 2
    time_walking = 3
    speed_walking = 6
    total_time = time_bathing + time_blowdrying + (time_walking / speed_walking)
    result = total_time
    return result

print(solution())