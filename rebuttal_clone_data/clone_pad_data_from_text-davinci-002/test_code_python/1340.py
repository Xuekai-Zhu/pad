def solution():
     max_hours_per_day = 6
     hours_two_days = 1.5
     hours_next_two_days = max_hours_per_day / 2
     total_hours = (max_hours_per_day * 2) + (hours_two_days * 2) + (hours_next_two_days * 2)
     result = total_hours
     return result

print(solution())