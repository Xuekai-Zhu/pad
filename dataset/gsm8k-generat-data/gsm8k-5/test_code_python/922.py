def solution():
    # Calculate Cadence's earnings in her old company
    old_company_salary = 5000 * 36  # $5000 per month for 36 months (3 years)

    # Calculate how long Cadence has worked in her new company
    new_company_time = 36 + 5  # Cadence has worked 5 months longer for her new company than her old company

    # Calculate Cadence's salary in her new company (20% more than her old salary)
    new_company_salary = 1.2 * 5000 * new_company_time

    # Calculate the total amount Cadence has earned in both companies
    total_earnings = old_company_salary + new_company_salary
    result = total_earnings
    return result

print(solution())