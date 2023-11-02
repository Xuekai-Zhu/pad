def solution():
    total_weeks = 104 # 2 years x 52 weeks per year
    allowance_per_week_first_year = 50
    job_pay_per_hour_second_year = 9
    hours_per_week_second_year = 30
    personal_spending_per_week = 35
    car_price = 15000
    
    # Calculate total savings from allowance in the first year
    total_allowance_savings = allowance_per_week_first_year * 52
    
    # Calculate total savings from job in the second year
    total_job_savings = job_pay_per_hour_second_year * hours_per_week_second_year * 52
    
    # Calculate total spending on personal expenses for 2 years
    total_personal_spending = personal_spending_per_week * total_weeks
    
    # Calculate total savings after accounting for personal expenses
    total_savings = total_allowance_savings + total_job_savings - total_personal_spending
    
    # Calculate remaining amount needed to buy the car
    remaining_amount = car_price - total_savings
    result = remaining_amount
    return result

print(solution())