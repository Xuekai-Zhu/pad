def solution():
    snowflake_stamps = 11
    truck_stamps = snowflake_stamps + 9  # bought 9 more truck stamps than snowflake stamps
    rose_stamps = truck_stamps - 13  # bought 13 fewer rose stamps than truck stamps
    total_stamps = snowflake_stamps + truck_stamps + rose_stamps
    result = total_stamps
    return result

print(solution())