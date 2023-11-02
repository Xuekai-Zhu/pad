def solution():
     hours_recommended = 2
     hours_used = 0.75
     minutes_used = 45
     minutes_remaining = (hours_recommended - hours_used) * 60
     result = minutes_remaining - minutes_used

     return result

print(solution())