def solution():
     points_scored_home = 62
     points_scored_away_1 = points_scored_home / 2
     points_scored_away_2 = points_scored_away_1 + 18
     points_scored_away_3 = points_scored_away_2 + 2
     points_needed = points_scored_home * 4 - (points_scored_away_1 + points_scored_away_2 + points_scored_away_3)
     result = points_needed
     return result

print(solution())