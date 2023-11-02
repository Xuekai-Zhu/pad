def solution():
     yards_per_dress = 5.5
     total_yards_needed = yards_per_dress * 4
     feet_on_hand = 7
     conversion = feet_on_hand / 3
     total_needed = total_yards_needed - conversion
     result = total_needed
     return result

print(solution())