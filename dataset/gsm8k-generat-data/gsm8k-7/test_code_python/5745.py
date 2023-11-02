def solution():
    standing_time = 10  # minutes
    sitting_time = 5  # minutes
    total_time = 120  # minutes

    # Calculate the total number of standing and sitting cycles Barry can complete
    total_cycles = total_time // (standing_time + sitting_time)

    # Calculate the number of standing cycles Barry can complete
    standing_cycles = total_cycles // 2

    result = standing_cycles
    return result

print(solution())