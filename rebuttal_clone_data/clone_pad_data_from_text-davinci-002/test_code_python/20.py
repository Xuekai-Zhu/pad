def solution():
     """Bella bought stamps at the post office. Some of the stamps had a snowflake design, some had a truck design, and some had a rose design. Bella bought 11 snowflake stamps. She bought 9 more truck stamps than snowflake stamps, and 13 fewer rose stamps than truck stamps. How many stamps did Bella buy in all?"""
     snowflake_stamps = 11
     truck_stamps = snowflake_stamps + 9
     rose_stamps = truck_stamps - 13
     total_stamps = snowflake_stamps + truck_stamps + rose_stamps
     
     result = total_stamps
     return result

print(solution())