def solution():
    
    basic_salary = 1250
    commission_rate = 0.10
    total_sales = 23600
    commission_earned = total_sales * commission_rate
    total_earnings = basic_salary + commission_earned
    savings = total_earnings * 0.20
    expenses = total_earnings - savings
    result = expenses
    return result

print(solution())