def solution():
     hours_per_day = 5
     days_per_month = 30
     total_hours_trained = hours_per_day * days_per_month
     additional_days = 12
     additional_hours = hours_per_day * additional_days
     total_hours = total_hours_trained + additional_hours
     return total_hours

print(solution())