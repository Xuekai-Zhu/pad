def solution():
    """James joins a football team and becomes the star. He scores 4 touchdowns per game and each touchdown is worth 6 points. There are 15 games in the season. He also manages to score 2 point conversions 6 times during the season. The old record was 300 points during the season. How many points did James beat the old record by?"""
    # Define the number of games in the season
    games = 15

    # Calculate the number of touchdowns and 2-point conversions
    touchdowns = games * 4
    conversions = 6

    # Calculate the total number of points scored
    total_points = touchdowns * 6 + conversions * 2

    # Calculate the number of points James beat the old record by
    old_record = 300
    points_beat = total_points - old_record

    # return the result
    result = points_beat
    return result

print(solution())