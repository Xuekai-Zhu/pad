def solution():
    total_employees = 450
    employees_laid_off = total_employees / 3
    remaining_employees = total_employees - employees_laid_off
    monthly_salary = 2000
    total_monthly_salary = remaining_employees * monthly_salary
    result = total_monthly_salary
    return result

print(solution())