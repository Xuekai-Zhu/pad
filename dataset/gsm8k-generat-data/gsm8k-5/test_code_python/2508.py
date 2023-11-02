def solution():
    # Initialize the number of employees and the number of employees laid off
    num_employees = 1000
    num_laid_off = 0

    # Iterate through the three rounds of layoffs
    for i in range(3):
        num_remaining = num_employees - num_laid_off
        num_laid_off_round = round(num_remaining * 0.1)
        num_laid_off += num_laid_off_round

    result = num_laid_off
    return result

print(solution())