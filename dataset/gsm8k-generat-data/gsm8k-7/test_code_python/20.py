def solution():
    num_snowflake_stamps = 11

    num_truck_stamps = num_snowflake_stamps + 9

    num_rose_stamps = num_truck_stamps - 13

    total_stamps = num_snowflake_stamps + num_truck_stamps + num_rose_stamps
    result = total_stamps
    return result

print(solution())