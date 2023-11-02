def solution():
     days_sleeping_6_hours = 5
     days_sleeping_10_hours = 2
     hours_sleeping_6_hours = 6
     hours_sleeping_10_hours = 10
     total_hours_sleeping = (days_sleeping_6_hours * hours_sleeping_6_hours) + (days_sleeping_10_hours * hours_sleeping_10_hours)
     result = total_hours_sleeping
     return result

print(solution())