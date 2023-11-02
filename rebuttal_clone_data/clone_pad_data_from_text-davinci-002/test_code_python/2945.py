def solution():
     minutes_per_move_polly = 28 / 60
     minutes_per_move_peter = 40 / 60
     moves_in_match = 30
     total_minutes = minutes_per_move_polly + minutes_per_move_peter
     result = total_minutes * moves_in_match
     return result

print(solution())