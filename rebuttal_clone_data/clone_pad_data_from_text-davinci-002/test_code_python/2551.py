def solution():
     old_record = 257
     points_needed = 17
     points_scored = old_record + points_needed
     three_pointers_scored = points_scored - 9
     three_pointers_normally = 2
     three_pointers_in_game = three_pointers_scored - three_pointers_normally
     result = three_pointers_in_game
     return result

print(solution())