def solution():
    """The total number of employees in a company is 450, and each employee earns $2000 per month. If the company laid off 1/3 of its employees due to tough economic times, calculate the total amount of money the company paid to the remaining employees."""
    # Define the number of employees and their monthly salary
    num_employees = 450
    monthly_salary = 2000

    # Calculate the number of employees remaining after layoffs
    remaining_employees = num_employees - (num_employees / 3)

    # Calculate the total amount paid to the remaining employees
    total_payment = remaining_employees * monthly_salary

    result = total_payment
    return result

print(solution())