def solution():
     total_cows = 18
     black_cows = 5 + (total_cows / 2)
     not_black_cows = total_cows - black_cows
     result = not_black_cows
     return result

print(solution())