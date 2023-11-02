def solution():
    time_to_warm = 1
    time_to_shape = 15
    time_to_proof = 2
    time_to_bake = 30
    time_to_cool = 15
    opening_time = 6
    start_time = opening_time + time_to_warm + time_to_shape + time_to_proof + time_to_bake + time_to_cool
    result = start_time
    return result

print(solution())