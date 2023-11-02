def solution():
    """Hillary's teacher assigned 1 hour of reading during the weekend. On Friday night, Hillary read for 16 minutes. On Saturday she read for 28 minutes. How many minutes does Hillary have to read on Sunday to complete the assignment?"""
    total_reading_time = 60
    friday_reading_time = 16
    saturday_reading_time = 28
    remaining_reading_time = total_reading_time - friday_reading_time - saturday_reading_time
    result = remaining_reading_time
    return result

print(solution())