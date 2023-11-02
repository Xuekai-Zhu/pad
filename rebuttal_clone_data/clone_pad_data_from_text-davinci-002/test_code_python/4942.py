def solution():
     points_total = 311
     points_combined = 188
     points_remaining = points_total - points_combined
     points_per_player = points_remaining / 3
     result = points_per_player
     return result

print(solution())