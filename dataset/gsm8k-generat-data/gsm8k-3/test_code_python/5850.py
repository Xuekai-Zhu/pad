def solution():
    """The total number of employees in a company is 450, and each employee earns $2000 per month. If the company laid off 1/3 of its employees due to tough economic times, calculate the total amount of money the company paid to the remaining employees."""
    # Define the number of employees and their monthly salary
    NUM_EMPLOYEES = 450
    MONTHLY_SALARY = 2000

    # Calculate the number of employees after the layoffs
    remaining_employees = NUM_EMPLOYEES * (2/3)

    # Calculate the total amount of money paid to the remaining employees
    total_salary = remaining_employees * MONTHLY_SALARY

    # Display the total salary paid
    result = total_salary
    return result

print(solution())