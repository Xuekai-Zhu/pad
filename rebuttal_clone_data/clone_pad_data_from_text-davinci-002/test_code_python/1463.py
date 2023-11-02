def solution():
    stairs_per_flight = 20
    seconds_per_stair = 11
    total_stairs = stairs_per_flight * 20
    total_seconds = total_stairs * seconds_per_stair
    remaining_seconds = total_seconds - 165
    result = remaining_seconds
    return result

print(solution())