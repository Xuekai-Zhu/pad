def solution():
    
    basic_salary = 1250
    commission_rate = 0.1
    total_sales = 23600
    commission = commission_rate * total_sales
    total_earnings = basic_salary + commission
    savings = 0.2 * total_earnings
    expenses = total_earnings - savings
    result = expenses
    return result

print(solution())