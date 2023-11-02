def solution():
    """Brayden and Gavin were playing touch football against Cole and Freddy. Touchdowns were worth 7 points. Brayden and Gavin scored 7 touchdowns. Cole and Freddy's team scored 9 touchdowns. How many more points did Cole and Freddy have than Brayden and Gavin?"""
    touchdowns_brayden_gavin = 7
    touchdowns_cole_freddy = 9
    points_per_touchdown = 7
    total_points_brayden_gavin = touchdowns_brayden_gavin * points_per_touchdown
    total_points_cole_freddy = touchdowns_cole_freddy * points_per_touchdown
    point_difference = total_points_cole_freddy - total_points_brayden_gavin
    result = point_difference
    return result

print(solution())