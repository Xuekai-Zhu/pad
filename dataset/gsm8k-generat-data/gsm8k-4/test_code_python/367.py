def solution():
    """Emily makes $1,000,000 per year. If she has 10 employees who make $20,000 per year, how much would her salary be if she took part of her salary to make sure all of her employees make $35,000 per year."""
    # Define Emily's salary and the number of employees
    emily_salary = 1000000
    num_employees = 10

    # Define the original and new employee salaries
    original_salary = 20000
    new_salary = 35000

    # Calculate the total amount needed to increase all employee salaries
    total_increase = (new_salary - original_salary) * num_employees

    # Determine the amount Emily needs to decrease her salary by to cover the total increase
    emily_sacrifice = total_increase / (1 - 1/11)

    # Calculate Emily's new salary
    new_emily_salary = emily_salary - emily_sacrifice

    result = new_emily_salary
    return result

print(solution())