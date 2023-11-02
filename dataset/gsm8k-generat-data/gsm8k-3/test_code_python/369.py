def solution():
    """Emily makes $1,000,000 per year. If she has 10 employees who make $20,000 per year, how much would her salary be if she took part of her salary to make sure all of her employees make $35,000 per year."""
    # Define Emily's salary and the original salary of each employee
    emily_salary = 1000000
    employee_salary = 20000

    # Define the desired salary for each employee
    desired_salary = 35000

    # Calculate the total amount needed to increase each employee's salary
    total_increase = (desired_salary - employee_salary) * 10

    # Calculate Emily's new salary after taking the necessary amount to increase her employees' salaries
    new_salary = emily_salary - total_increase

    # Display Emily's new salary
    result = new_salary
    return result

print(solution())