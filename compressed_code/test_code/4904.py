def solution():
    
    regular_customers_per_hour = 175
    holiday_customers_per_hour = regular_customers_per_hour * 2
    holiday_hours = 8
    total_holiday_customers = holiday_customers_per_hour * holiday_hours
    result = total_holiday_customers
    return result

print(solution())