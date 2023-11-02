def solution():
    # Calculate how many teachers leave after 1 hour
    left_after_1_hour = 0.5 * 60

    # Calculate how many teachers remain after 1 hour
    remain_after_1_hour = 60 - left_after_1_hour

    # Calculate how many teachers quit before lunch
    quit_before_lunch = 0.3 * remain_after_1_hour

    # Calculate how many teachers are left after lunch
    left_after_lunch = remain_after_1_hour - quit_before_lunch

    result = left_after_lunch
    return result

print(solution())