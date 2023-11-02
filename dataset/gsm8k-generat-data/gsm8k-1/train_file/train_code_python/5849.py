def solution():
    """The total number of employees in a company is 450, and each employee earns $2000 per month. If the company laid off 1/3 of its employees due to tough economic times, calculate the total amount of money the company paid to the remaining employees."""
    num_employees = 450
    salary_per_month = 2000
    remaining_employees = num_employees - (num_employees / 3)
    total_cost = remaining_employees * salary_per_month
    result = total_cost
    return result

print(solution())