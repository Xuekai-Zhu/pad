def solution():
     points_per_round = 5
     rounds_played = 30
     taro_points = rounds_played * points_per_round * (3/5) - 4
     vlad_points = taro_points / (3/5)
     total_points = taro_points + vlad_points
     result = vlad_points
     return result

print(solution())