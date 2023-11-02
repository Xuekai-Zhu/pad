def solution():
     minutes_in_an_hour = 60
     minutes_per_day_weekdays = 30
     minutes_per_day_weekends = 120
     days_in_a_week = 7
     weeks_in_a_year = 52
     tv_minutes_weekdays = minutes_per_day_weekdays * days_in_a_week
     tv_minutes_weekends = minutes_per_day_weekends * (days_in_a_week / 2)
     total_tv_minutes = (tv_minutes_weekdays * (weeks_in_a_year / 2)) + (tv_minutes_weekends * (weeks_in_a_year / 2))
     tv_hours = total_tv_minutes / minutes_in_an_hour
     result = tv_hours
     return result

print(solution())