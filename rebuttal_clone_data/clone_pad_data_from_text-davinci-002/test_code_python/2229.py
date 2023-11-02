def solution():
     dollars_per_hour = 2
     hours_per_week = 4
     days_worked_per_week = 3
     weeks_worked = 4
     total_hours = hours_per_week * days_worked_per_week * weeks_worked
     total_earnings = total_hours * dollars_per_hour
     result = total_earnings
     return result

print(solution())