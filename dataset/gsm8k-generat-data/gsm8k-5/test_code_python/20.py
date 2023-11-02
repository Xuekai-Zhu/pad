def solution():
    snowflake_stamps = 11  # Bella bought 11 snowflake stamps
    truck_stamps = snowflake_stamps + 9  # Bella bought 9 more truck stamps than snowflake stamps
    rose_stamps = truck_stamps - 13  # Bella bought 13 fewer rose stamps than truck stamps

    # Calculate the total number of stamps Bella bought
    total_stamps = snowflake_stamps + truck_stamps + rose_stamps
    result = total_stamps
    return result

print(solution())