def solution():
    monthly_salary = 6000
    salary_increase = 0.3  # 30% increase
    num_years = 3

    # Calculate the salary after 1 year
    new_salary = monthly_salary + (monthly_salary * salary_increase)

    # Calculate the total earnings after 3 years
    total_earnings = (new_salary * 12 * num_years) + (monthly_salary * 12 * (num_years - 1))
    result = total_earnings
    return result

print(solution())