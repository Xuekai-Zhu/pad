def solution():
     days_in_month = 31
     days_not_walked = 4
     days_walked = days_in_month - days_not_walked
     miles_per_day = 4
     total_miles = days_walked * miles_per_day
     result = total_miles
     return result

print(solution())