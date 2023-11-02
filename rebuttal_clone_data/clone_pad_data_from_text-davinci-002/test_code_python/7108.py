def solution():
    jumps_per_minute_child = 30
    jumps_per_second_adult = 1
    total_jumps_child = jumps_per_minute_child * 60
    total_jumps_adult = jumps_per_second_adult * 60 * 60
    result = total_jumps_adult - total_jumps_child
    return result

print(solution())