def solution():
     antacids_per_day_indian = 3
     antacids_per_day_mexican = 2
     antacids_per_day_other = 1
     days_per_week_indian = 3
     days_per_week_mexican = 2
     days_per_month = 4
     antacids_per_month = (antacids_per_day_indian * days_per_week_indian * days_per_month) + (antacids_per_day_mexican * days_per_week_mexican * days_per_month) + (antacids_per_day_other * (days_per_month - (days_per_week_indian + days_per_week_mexican)))
     result = antacids_per_month
     return result

print(solution())