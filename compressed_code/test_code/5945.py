def solution():
    
    savings_per_month = 25
    total_months_saved = 2 * 12
    total_savings = savings_per_month * total_months_saved
    spending = 400
    remaining_savings = total_savings - spending
    result = remaining_savings
    return result

print(solution())