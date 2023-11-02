def solution():
    salary_per_hour = 7.50
    commission_percentage = 16
    hours_worked = 160
    total_sales = 25000
    total_monthly_earnings = salary_per_hour * hours_worked + total_sales * (commission_percentage / 100)
    monthly_budget = total_monthly_earnings * 0.95
    insurance_allocation = total_monthly_earnings - monthly_budget
    result = insurance_allocation
    
    return result

print(solution())