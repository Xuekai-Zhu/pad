def solution():
    side_length = 15
    perimiter = side_length * 4
    rowing_speed = 2
    swimming_speed = 1
    time_to_swim_1_mile = 20
    time_to_row_1_mile = time_to_swim_1_mile / rowing_speed
    time_to_row_perimiter = perimiter * time_to_row_1_mile
    time_to_row_perimiter_in_hours = time_to_row_perimiter / 60
    result = time_to_row_perimiter_in_hours
    
    return result

print(solution())