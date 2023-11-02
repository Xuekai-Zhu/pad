def solution():
    """James joins a football team and becomes the star. He scores 4 touchdowns per game and each touchdown is worth 6 points. There are 15 games in the season. He also manages to score 2 point conversions 6 times during the season. The old record was 300 points during the season. How many points did James beat the old record by?"""
    touchdowns_per_game = 4
    points_per_touchdown = 6
    games_in_season = 15
    conversions = 6
    old_record = 300
    
    total_touchdown_points = touchdowns_per_game * points_per_touchdown * games_in_season
    conversion_points = conversions * 2
    total_points = total_touchdown_points + conversion_points
    
    record_beaten_by = total_points - old_record
    result = record_beaten_by
    
    return result

print(solution())