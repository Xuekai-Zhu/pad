def solution():
    hours_worked = 160
    hourly_salary = 7.5
    total_sales = 25000
    commission_rate = 0.16
    monthly_budget_percentage = 0.95

    # Calculate Kristy's earnings from her hourly salary
    hourly_earnings = hours_worked * hourly_salary

    # Calculate Kristy's earnings from her commission
    commission_earnings = total_sales * commission_rate

    # Calculate Kristy's total earnings
    total_earnings = hourly_earnings + commission_earnings

    # Calculate Kristy's monthly budget for food, clothing, rent, transportation, bills and savings
    monthly_budget = total_earnings * monthly_budget_percentage

    # Calculate Kristy's insurance budget
    insurance_budget = total_earnings - monthly_budget
    result = insurance_budget
    return result

print(solution())