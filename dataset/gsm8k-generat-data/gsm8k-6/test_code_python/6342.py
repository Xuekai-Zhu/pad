def solution():
    # Calculate the number of customers during the holiday season
    customers_per_hour = 175
    holiday_customers_per_hour = customers_per_hour * 2
    holiday_hours = 8
    total_holiday_customers = holiday_customers_per_hour * holiday_hours
    result = total_holiday_customers
    return result

print(solution())