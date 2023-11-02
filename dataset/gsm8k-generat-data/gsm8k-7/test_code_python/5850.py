def solution():
    num_employees = 450
    monthly_salary = 2000
    layoff_fraction = 1/3

    # Calculate the total number of employees who were laid off
    num_laid_off = round(num_employees * layoff_fraction)

    # Calculate the total number of remaining employees
    num_remaining = num_employees - num_laid_off

    # Calculate the total amount of money paid to the remaining employees
    total_paid = num_remaining * monthly_salary
    result = total_paid
    return result

print(solution())