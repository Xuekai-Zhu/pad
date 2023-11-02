def solution():
    touchdown_points = 7

    b_g_touchdowns = 7
    c_f_touchdowns = 9

    # Calculate the total points scored by Brayden and Gavin
    b_g_points = b_g_touchdowns * touchdown_points

    # Calculate the total points scored by Cole and Freddy
    c_f_points = c_f_touchdowns * touchdown_points

    # Calculate the difference in points between the two teams
    point_difference = c_f_points - b_g_points
    result = point_difference
    return result

print(solution())