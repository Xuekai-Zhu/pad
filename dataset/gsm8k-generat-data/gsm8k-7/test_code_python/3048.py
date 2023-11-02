def solution():
    initial_num_sub_teachers = 60
    walkout_rate_after_1_hr = 0.5
    quit_rate_before_lunch = 0.3

    # Calculate the number of teachers who walk out after 1 hour
    num_walkouts = initial_num_sub_teachers * walkout_rate_after_1_hr

    # Calculate the number of teachers who remain after 1 hour
    num_remain_after_1_hr = initial_num_sub_teachers - num_walkouts

    # Calculate the number of teachers who quit before lunch
    num_quit_before_lunch = num_remain_after_1_hr * quit_rate_before_lunch

    # Calculate the number of teachers who will be left after lunch
    num_left_after_lunch = num_remain_after_1_hr - num_quit_before_lunch
    result = num_left_after_lunch
    return result

print(solution())