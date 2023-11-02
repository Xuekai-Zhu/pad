def solution():
     pills_per_day = 1
     days_in_week = 7
     weeks = 2
     pills_used = pills_per_day * days_in_week * weeks
     pills_left = 120 * 3 + 30 * 2 - pills_used
     result = pills_left
     return result

print(solution())