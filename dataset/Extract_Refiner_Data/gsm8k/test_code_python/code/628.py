def solution():
    
    snowflake_stamps = 16
    truck_stamps = snowflake_stamps + 3
    rose_stamps = truck_stamps - 9
    total_stamps = snowflake_stamps + truck_stamps + rose_stamps
    result = total_stamps
    return result

print(solution())