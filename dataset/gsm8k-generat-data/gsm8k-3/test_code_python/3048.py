def solution():
    """50% of substitute teachers walk out after 1 hour of teaching. 30% of the remainder quit before lunch. If 60 substitute teachers show up at 7 AM, how many will be left after lunch?"""
    # Calculate the number of teachers who walk out after 1 hour
    walk_out_1_hour = 60 * 0.5

    # Calculate the number of teachers who remain after 1 hour
    remain_1_hour = 60 - walk_out_1_hour

    # Calculate the number of teachers who quit before lunch
    quit_before_lunch = remain_1_hour * 0.3

    # Calculate the number of teachers who remain after lunch
    remain_after_lunch = remain_1_hour - quit_before_lunch

    # Display the number of teachers who remain after lunch
    result = remain_after_lunch
    return result

print(solution())