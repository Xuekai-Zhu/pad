def solution():
    # Calculate the number of employees who were laid off
    laid_off_employees = 450 * (1/3)

    # Calculate the number of remaining employees
    remaining_employees = 450 - laid_off_employees

    # Calculate the total amount of money the company pays to the remaining employees
    total_salary = remaining_employees * 2000

    result = total_salary
    return result

print(solution())