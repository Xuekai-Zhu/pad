def solution():
    touchdowns_per_game = 4  # James scores 4 touchdowns per game
    points_per_touchdown = 6  # Each touchdown is worth 6 points
    games_per_season = 15  # There are 15 games in the season
    two_point_conversions = 6  # James scores 2 point conversions 6 times during the season

    # Total points scored by James in the season
    total_points = (touchdowns_per_game * points_per_touchdown * games_per_season) + (two_point_conversions * 2)

    # The old record was 300 points during the season
    old_record = 300

    # Calculate the points James beat the old record by
    record_beaten_by = total_points - old_record
    result = record_beaten_by
    return result

print(solution())