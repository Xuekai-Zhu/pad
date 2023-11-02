def solution():
    
    starting_teachers = 60
    first_hour_dropout = starting_teachers * 0.5
    remaining_teachers = starting_teachers - first_hour_dropout
    pre_lunch_dropout = remaining_teachers * 0.3
    lunch_leavers = first_hour_dropout + pre_lunch_dropout
    remaining_after_lunch = starting_teachers - lunch_leavers
    result = remaining_after_lunch
    return result

print(solution())