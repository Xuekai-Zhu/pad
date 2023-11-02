def solution():
    
    hours_per_day = 5
    days_in_month = 30
    total_hours_month = hours_per_day * days_in_month
    additional_days = 12
    total_hours = total_hours_month + (additional_days * hours_per_day)
    result = total_hours
    return result

print(solution())