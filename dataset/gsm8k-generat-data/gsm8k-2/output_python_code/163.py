def solution():
    """James joins a football team and becomes the star. He scores 4 touchdowns per game and each touchdown is worth 6 points. There are 15 games in the season. He also manages to score 2 point conversions 6 times during the season. The old record was 300 points during the season. How many points did James beat the old record by?"""
    touchdowns_per_game = 4
    touchdown_points = 6
    conversion_points = 2
    total_games = 15
    total_touchdowns = touchdowns_per_game * total_games
    total_conversion_points = conversion_points * 6
    total_points = (total_touchdowns * touchdown_points) + total_conversion_points
    old_record = 300
    points_above_record = total_points - old_record
    result = points_above_record
    return result

print(solution())