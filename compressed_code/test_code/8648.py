def solution():
    
    fiona_hours_per_week = 40
    john_hours_per_week = 30
    jeremy_hours_per_week = 25
    hourly_rate = 20
    total_hours_per_week = fiona_hours_per_week + john_hours_per_week + jeremy_hours_per_week
    total_monthly_pay = total_hours_per_week * hourly_rate * 4
    result = total_monthly_pay
    return result

print(solution())