def solution():
    total_work_time = 240
    water_break_frequency = 20
    sitting_break_frequency = 120

    water_breaks = total_work_time // water_break_frequency
    sitting_breaks = total_work_time // sitting_break_frequency

    difference = water_breaks - sitting_breaks
    result = difference
    return result

print(solution())