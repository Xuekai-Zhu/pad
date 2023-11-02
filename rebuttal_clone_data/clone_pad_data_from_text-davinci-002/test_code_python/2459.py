def solution():
    workers = 3
    chairs_per_hour = 4
    hours = 6
    chairs_produced = workers * chairs_per_hour + (hours // 6)
    result = chairs_produced
    return result

print(solution())