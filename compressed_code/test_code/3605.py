def solution():
    
    earnings_per_customer = 18
    monthly_expenses = 280
    num_customers = 80
    total_earnings = earnings_per_customer * num_customers
    recreation_allocation = 0.2 * total_earnings
    total_expenses = monthly_expenses + recreation_allocation
    total_savings = total_earnings - total_expenses
    result = total_savings
    return result

print(solution())