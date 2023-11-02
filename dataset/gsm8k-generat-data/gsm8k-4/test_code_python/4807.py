def solution():
    """Brayden and Gavin were playing touch football against Cole and Freddy. Touchdowns were worth 7 points. Brayden and Gavin scored 7 touchdowns. Cole and Freddy's team scored 9 touchdowns. How many more points did Cole and Freddy have than Brayden and Gavin?"""
    # Define the points per touchdown
    POINTS_PER_TOUCHDOWN = 7

    # Calculate the total points scored by Brayden and Gavin
    bg_points = POINTS_PER_TOUCHDOWN * 7

    # Calculate the total points scored by Cole and Freddy
    cf_points = POINTS_PER_TOUCHDOWN * 9

    # Calculate the difference in points
    point_difference = cf_points - bg_points

    # Return the result
    result = point_difference
    return result

print(solution())