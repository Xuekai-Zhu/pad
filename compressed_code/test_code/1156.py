def solution():
    
    hourly_rate = 7.5
    commission_rate = 0.16
    hours_worked = 160
    items_sold = 25000

    basic_salary = hourly_rate * hours_worked
    commission = commission_rate * items_sold
    total_earnings = basic_salary + commission

    monthly_budget = 0.95 * total_earnings
    insurance_allocation = total_earnings - monthly_budget

    return insurance_allocation

print(solution())