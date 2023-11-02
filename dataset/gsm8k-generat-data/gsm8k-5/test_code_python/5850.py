def solution():
    total_employees = 450  # Total number of employees in the company
    monthly_salary = 2000  # Monthly salary earned by each employee
    laid_off_employees = total_employees / 3  # Number of employees laid off
    remaining_employees = total_employees - laid_off_employees  # Number of employees remaining
    total_salary_paid = remaining_employees * monthly_salary  # Total amount of money paid to remaining employees
    result = total_salary_paid
    return result

print(solution())