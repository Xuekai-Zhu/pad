def solution():
    
    first_month_pay = 200
    second_month_pay = first_month_pay + 150
    hourly_rate = 10
    first_month_hours = first_month_pay/hourly_rate
    second_month_hours = second_month_pay/hourly_rate
    total_hours = first_month_hours + second_month_hours
    result = total_hours
    return result

print(solution())