def solution():
    
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