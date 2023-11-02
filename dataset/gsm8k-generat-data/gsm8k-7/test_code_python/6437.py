def solution():
    materials_time = 6  # minutes
    manufacture_time = 9  # minutes
    robots = 10
    total_time = 5*60  # minutes in 5 hours

    total_batteries = (total_time / (materials_time + manufacture_time)) * robots
    result = total_batteries
    return result

print(solution())