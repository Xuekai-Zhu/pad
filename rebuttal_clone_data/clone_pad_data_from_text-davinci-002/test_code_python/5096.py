def solution():
     pages_read_weekday = 10
     pages_read_weekend = 20
     days_in_week = 7
     pages_read_per_day = (pages_read_weekday * 5) + (pages_read_weekend * 2)
     pages_read_per_week = pages_read_per_day * days_in_week
     result = pages_read_per_week * 2
     return result

print(solution())