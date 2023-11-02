def solution():
    
    hourly_wage = 12.00
    customers_per_hour = 20
    tip_per_customer = 1.25
    total_tips = customers_per_hour * tip_per_customer
    total_earnings = hourly_wage + total_tips
    result = total_earnings
    return result

print(solution())