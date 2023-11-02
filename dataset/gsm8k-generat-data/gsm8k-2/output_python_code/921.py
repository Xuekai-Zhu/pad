def solution():
    """Cadence has worked for her new company five months longer than she worked for her old company. If she worked at her old company for 3 years earning $5000 per month, and she's now earning 20% more in the new company, calculate the total amount of money she's earned in both companies in the period she's worked for them?"""
    old_company_months = 3 * 12
    old_company_salary = 5000
    old_company_earnings = old_company_months * old_company_salary

    new_company_months = old_company_months + 5
    new_company_salary = 1.2 * old_company_salary
    new_company_earnings = new_company_months * new_company_salary

    total_earnings = old_company_earnings + new_company_earnings
    result = total_earnings
    return result

print(solution())