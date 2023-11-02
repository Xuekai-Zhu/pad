def solution():
    commission_rate = 12
    total_sales = 24000
    personal_percentage = 60
    commission = total_sales * (commission_rate / 100)
    personal_expenses = commission * (personal_percentage / 100)
    savings = commission - personal_expenses
    result = savings
    
    return result

print(solution())