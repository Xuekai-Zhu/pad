def solution():
     days_per_month = 30
     days_per_week = 7
     months_with_15_days = 4
     months_with_3_days = 8
     total_days = (days_per_month * months_with_15_days) + (days_per_week * months_with_3_days)
     average_days = total_days / 12
     result = average_days
     return result

print(solution())