def solution():
    num_employees = 10  # Emily has 10 employees
    current_employee_salary = 20000  # Emily's current employees make $20,000 per year
    desired_employee_salary = 35000  # Emily wants her employees to make $35,000 per year

    # Calculate the total salary Emily needs to pay her employees
    total_salary_needed = num_employees * desired_employee_salary

    # Calculate how much Emily needs to reduce her own salary in order to pay her employees the desired amount
    salary_reduction = (total_salary_needed - (num_employees * current_employee_salary)) / 2

    # Calculate Emily's new salary after the reduction
    new_salary = 1000000 - salary_reduction
    result = new_salary
    return result

print(solution())