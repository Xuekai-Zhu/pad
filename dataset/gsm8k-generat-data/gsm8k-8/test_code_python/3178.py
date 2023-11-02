def solution():
    circuit_length = 365
    morning_runs = 7
    afternoon_runs = 3

    morning_distance = morning_runs * circuit_length
    afternoon_distance = afternoon_runs * circuit_length

    total_distance = morning_distance + afternoon_distance
    result = total_distance
    return result

print(solution())