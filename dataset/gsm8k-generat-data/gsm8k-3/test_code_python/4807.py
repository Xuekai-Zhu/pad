def solution():
    """Brayden and Gavin were playing touch football against Cole and Freddy. Touchdowns were worth 7 points. Brayden and Gavin scored 7 touchdowns. Cole and Freddy's team scored 9 touchdowns. How many more points did Cole and Freddy have than Brayden and Gavin?"""
    # Define the points per touchdown
    TOUCHDOWN_POINTS = 7

    # Calculate Brayden and Gavin's total points
    bg_points = 7 * TOUCHDOWN_POINTS

    # Calculate Cole and Freddy's total points
    cf_points = 9 * TOUCHDOWN_POINTS

    # Calculate the difference in points
    point_difference = cf_points - bg_points

    # Display the point difference
    result = point_difference
    return result

print(solution())