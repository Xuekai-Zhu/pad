def solution():
    omar_height = 240
    omar_time = 12

    jasper_height = 600
    jasper_speed = 3 * (omar_height / omar_time)

    jasper_time = jasper_height / jasper_speed
    result = jasper_time
    return result

print(solution())