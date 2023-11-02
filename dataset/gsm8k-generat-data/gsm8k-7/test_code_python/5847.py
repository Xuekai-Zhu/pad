def solution():
    hourly_wage = 8.5
    num_hours_per_day = 8
    num_days_per_month = 20
    num_months_per_year = 12

    # Calculate the total hours Ursula works in a month
    total_hours_per_month = num_hours_per_day * num_days_per_month

    # Calculate Ursula's monthly salary
    monthly_salary = hourly_wage * total_hours_per_month

    # Calculate Ursula's annual salary
    annual_salary = monthly_salary * num_months_per_year
    result = annual_salary
    return result

print(solution())