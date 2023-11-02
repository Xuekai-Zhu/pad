def solution():
    
    total_employees = 1000
    percent_layoff = 0.1
    employees_laid_off = 0
    for i in range(3):
        employees_remaining = total_employees - employees_laid_off
        employees_laid_off += round(employees_remaining * percent_layoff)
    result = employees_laid_off
    return result

print(solution())