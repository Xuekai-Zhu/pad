def solution():
    # Calculate the depth of the snowdrift on the first day
    # Work backwards from the fourth day
    depth_fourth_day = 34
    depth_third_day = depth_fourth_day - 18
    depth_second_day = depth_third_day / 2
    depth_first_day = depth_second_day + 6
    result = depth_first_day
    return result

print(solution())