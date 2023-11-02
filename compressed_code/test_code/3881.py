def solution():
    
    sales_amount = 2500
    commission_rate = 0.02
    commission_earnings = sales_amount * commission_rate
    basic_salary = 240
    total_earnings = commission_earnings + basic_salary
    savings_rate = 0.1
    total_savings = total_earnings * savings_rate
    result = total_savings
    return result

print(solution())