def solution():
     total_capacity = 50
     daily_rain = 800
     daily_river = 1700
     days_needed = total_capacity / (daily_rain + daily_river)
     result = days_needed
     return result

print(solution())