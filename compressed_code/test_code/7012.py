def solution():
    
    hours_per_week = 40
    hourly_rate_current_job = 30
    hourly_rate_freelancer = 40
    extra_FICA_taxes = 25 * 4
    healthcare_premiums = 400
    monthly_income_current_job = hours_per_week * hourly_rate_current_job * 4
    monthly_income_freelancer = hours_per_week * hourly_rate_freelancer * 4 - extra_FICA_taxes - healthcare_premiums
    extra_monthly_income = monthly_income_freelancer - monthly_income_current_job
    result = extra_monthly_income
    return result

print(solution())