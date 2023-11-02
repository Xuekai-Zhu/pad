def solution():
    """James joins a football team and becomes the star. He scores 4 touchdowns per game and each touchdown is worth 6 points. There are 15 games in the season. He also manages to score 2 point conversions 6 times during the season. The old record was 300 points during the season. How many points did James beat the old record by?"""
    # Define the number of touchdowns and games
    touchdowns_per_game = 4
    games = 15

    # Calculate the total number of touchdowns scored by James
    total_touchdowns = touchdowns_per_game * games

    # Calculate the total number of points scored by James from touchdowns
    touchdown_points = total_touchdowns * 6

    # Calculate the total number of points scored by James from 2 point conversions
    conversion_points = 6 * 2

    # Calculate the total number of points scored by James
    total_points = touchdown_points + (conversion_points*6)

    # Calculate the number of points James beat the old record by
    old_record = 300
    points_beat_old_record = total_points - old_record

    # return the result
    result = points_beat_old_record
    return result

print(solution())