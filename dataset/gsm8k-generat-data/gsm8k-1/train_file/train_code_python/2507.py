def solution():
    """A company has 1000 employees. There will be three rounds of layoffs. For each round of layoff, 10% of the remaining employees will be laid off. How many employees will be laid off in total?"""
    total_employees = 1000
    percent_layoff = 0.1
    employees_laid_off = 0
    for i in range(3):
        employees_remaining = total_employees - employees_laid_off
        employees_laid_off += round(employees_remaining * percent_layoff)
    result = employees_laid_off
    return result

print(solution())