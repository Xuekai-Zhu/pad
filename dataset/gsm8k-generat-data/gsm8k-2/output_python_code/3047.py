def solution():
    """50% of substitute teachers walk out after 1 hour of teaching. 30% of the remainder quit before lunch. If 60 substitute teachers show up at 7 AM, how many will be left after lunch?"""
    starting_teachers = 60
    first_hour_dropout = starting_teachers * 0.5
    remaining_teachers = starting_teachers - first_hour_dropout
    pre_lunch_dropout = remaining_teachers * 0.3
    lunch_leavers = first_hour_dropout + pre_lunch_dropout
    remaining_after_lunch = starting_teachers - lunch_leavers
    result = remaining_after_lunch
    return result

print(solution())