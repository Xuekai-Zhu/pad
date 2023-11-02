def solution():
    # Calculate the total salary of all employees before the raise
    employee_salary_before = 10 * 20000

    # Calculate the total salary needed for all employees to make $35,000 per year
    employee_salary_after = 10 * 35000

    # Calculate the amount Emily needs to give to make up the difference
    difference = employee_salary_after - employee_salary_before

    # Calculate Emily's new salary after giving the raise
    new_salary = 1000000 - difference

    result = new_salary
    return result

print(solution())