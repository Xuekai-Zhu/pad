def solution():
    
    first_month_income = 200
    second_month_income = first_month_income + 150
    total_income = first_month_income + second_month_income
    hourly_rate = 10
    total_hours = total_income / hourly_rate
    result = total_hours
    return result

print(solution())