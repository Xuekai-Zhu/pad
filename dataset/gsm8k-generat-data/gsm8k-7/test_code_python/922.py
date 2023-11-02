def solution():
    old_company_years = 3
    old_company_salary = 5000
    new_company_salary = 1.2 * old_company_salary

    # Calculate the total amount earned in the old company
    old_company_total = old_company_years * 12 * old_company_salary

    # Calculate the amount of time worked in the new company
    new_company_months = old_company_years * 12 + 5

    # Calculate the total earnings in the new company
    new_company_total = new_company_months * new_company_salary

    # Calculate the total earnings for both companies
    total_earnings = old_company_total + new_company_total
    result = total_earnings
    return result

print(solution())