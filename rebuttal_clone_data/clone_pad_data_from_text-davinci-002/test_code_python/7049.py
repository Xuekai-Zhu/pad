def solution():
    work_time_minutes = 240
    water_break_interval_minutes = 20
    sitting_break_interval_minutes = 120
    number_of_water_breaks = work_time_minutes / water_break_interval_minutes
    number_of_sitting_breaks = work_time_minutes / sitting_break_interval_minutes
    result = number_of_water_breaks - number_of_sitting_breaks
    return result

print(solution())