def solution():
     points_scored = 345
     games_played = 15
     free_throws = 4
     two_point_baskets = 5
     three_point_baskets = (points_scored - (games_played * (free_throws + two_point_baskets))) / games_played
     result = three_point_baskets
     return result

print(solution())