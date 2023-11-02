def solution():
    touchdowns_per_game = 4
    points_per_touchdown = 6
    num_games = 15
    extra_points = 6
    old_record = 300

    # Calculate the total number of touchdowns scored by James in the season
    total_touchdowns = touchdowns_per_game * num_games

    # Calculate the total number of points scored from touchdowns
    touchdown_points = total_touchdowns * points_per_touchdown

    # Calculate the total number of points scored from 2 point conversions
    conversion_points = extra_points * 2

    # Calculate the grand total number of points scored by James in the season
    total_points = touchdown_points + conversion_points

    # Calculate the number of points James beat the old record by
    point_difference = total_points - old_record
    result = point_difference
    return result

print(solution())