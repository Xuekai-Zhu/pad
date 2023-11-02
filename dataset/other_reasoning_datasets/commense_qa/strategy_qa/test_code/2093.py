def solution():
    driving_time_to_library = 0.5
    visiting_time_at_library = 2
    driving_time_to_six_flags = 3.5
    visiting_time_at_six_flags = 4
    total_time = driving_time_to_library + visiting_time_at_library + driving_time_to_six_flags + visiting_time_at_six_flags
    if total_time <= 24:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())