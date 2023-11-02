def solution():
    num_employees = 1000
    layoff_ratio = 0.1
    total_laid_off = 0
    for i in range(3):
        remaining_employees = num_employees - total_laid_off
        employees_laid_off = round(remaining_employees * layoff_ratio)
        total_laid_off += employees_laid_off
    result = total_laid_off
    return result

print(solution())