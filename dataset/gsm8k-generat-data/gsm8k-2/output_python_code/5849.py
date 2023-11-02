def solution():
    """The total number of employees in a company is 450, and each employee earns $2000 per month. If the company laid off 1/3 of its employees due to tough economic times, calculate the total amount of money the company paid to the remaining employees."""
    total_employees = 450
    monthly_salary = 2000
    remaining_employees = total_employees * 2/3
    total_salary = remaining_employees * monthly_salary
    result = total_salary
    return result

print(solution())