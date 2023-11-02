def solution():
     hours_per_week = 6
     days_per_week = 2
     hours_per_day = 3
     hourly_wage = 10
     total_hours = hours_per_week * days_per_week * hours_per_day
     total_earnings = total_hours * hourly_wage
     result = total_earnings
     return result

print(solution())