def solution():
     """James joins a football team and becomes the star. He scores 4 touchdowns per game and each touchdown is worth 6 points. There are 15 games in the season. He also manages to score 2 point conversions 6 times during the season. The old record was 300 points during the season. How many points did James beat the old record by?"""
     touchdowns_per_game = 4
     points_per_touchdown = 6
     games_in_season = 15
     total_touchdowns = touchdowns_per_game * games_in_season
     total_points = total_touchdowns * points_per_touchdown
     old_record = 300
     new_record = total_points
     difference = new_record - old_record
     result =  difference
     
     return result

print(solution())