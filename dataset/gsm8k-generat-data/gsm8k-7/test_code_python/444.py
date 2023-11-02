def solution():
    num_layups = 3
    layup_points = 1

    num_free_throws = 2
    free_throw_points = 2

    num_long_shots_reggie = 1
    long_shot_points = 3

    num_long_shots_brother = 4

    # Calculate the total number of points for Reggie
    reggie_points = (num_layups * layup_points) + (num_free_throws * free_throw_points) + \
                    (num_long_shots_reggie * long_shot_points)

    # Calculate the total number of points for Reggie's brother
    brother_points = num_long_shots_brother * long_shot_points

    # Calculate the difference in points between Reggie and his brother
    point_difference = brother_points - reggie_points
    result = point_difference
    return result

print(solution())