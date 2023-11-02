def solution():
    """A company has 1000 employees. There will be three rounds of layoffs. For each round of layoff, 10% of the remaining employees will be laid off. How many employees will be laid off in total?"""
    total_employees = 1000
    layoff_rate = 0.1
    total_laid_off = 0
    for i in range(3):
        remaining_employees = total_employees - total_laid_off
        current_layoff = round(remaining_employees * layoff_rate)
        total_laid_off += current_layoff

    result = total_laid_off
    return result

print(solution())