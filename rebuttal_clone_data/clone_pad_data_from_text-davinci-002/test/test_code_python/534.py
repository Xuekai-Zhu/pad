def solution():
    months_old_company = 3 * 12
    old_salary = 5000
    new_salary = old_salary * 1.2
    new_months = months_old_company + 5
    total_salary = old_salary * months_old_company + new_salary * new_months
    result = total_salary
    return result

print(solution())