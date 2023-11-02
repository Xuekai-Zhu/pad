def solution():
    
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