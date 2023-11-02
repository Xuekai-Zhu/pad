def solution():
    """Bella bought stamps at the post office. Some of the stamps had a snowflake design, some had a truck design, and some had a rose design. Bella bought 11 snowflake stamps. She bought 9 more truck stamps than snowflake stamps, and 13 fewer rose stamps than truck stamps. How many stamps did Bella buy in all?"""
    
    # Define the number of snowflake stamps Bella bought
    snowflake_stamps = 11
    
    # Define the number of truck stamps Bella bought
    truck_stamps = snowflake_stamps + 9
    
    # Define the number of rose stamps Bella bought
    rose_stamps = truck_stamps - 13
    
    # Calculate the total number of stamps Bella bought
    total_stamps = snowflake_stamps + truck_stamps + rose_stamps
    
    result = total_stamps
    return result

print(solution())