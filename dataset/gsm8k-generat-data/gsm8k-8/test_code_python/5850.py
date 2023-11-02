def solution():
    # Define the total number of employees and the amount each employee earns per month
    total_employees = 450
    monthly_salary = 2000

    # Calculate the number of employees who were laid off
    laid_off_employees = total_employees * 1/3

    # Calculate the number of remaining employees
    remaining_employees = total_employees - laid_off_employees

    # Calculate the total amount of money paid to the remaining employees
    total_paid = remaining_employees * monthly_salary
    result = total_paid
    return result

print(solution())