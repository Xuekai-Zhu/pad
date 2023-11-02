def solution():
    """A company has 500 employees, each paid $12 per hour, working 10 hours a day, five days a week, 4 weeks a month. In August, the amount of work increased, and the company hired 200 more people. How much money does the company pay in total per month after the new hires?"""
    # Define the initial number of employees and their salary
    initial_employees = 500
    initial_salary = 12

    # Calculate the total number of hours worked per month by each employee
    hours_per_day = 10
    days_per_week = 5
    weeks_per_month = 4
    total_hours_per_month = hours_per_day * days_per_week * weeks_per_month

    # Calculate the total salary paid to the initial employees per month
    initial_salary_per_month = initial_employees * initial_salary * total_hours_per_month

    # Calculate the total salary paid to the new hires per month
    new_hires = 200
    new_salary_per_month = new_hires * initial_salary * total_hours_per_month

    # Calculate the total salary paid per month after the new hires
    total_salary_per_month = initial_salary_per_month + new_salary_per_month

    result = total_salary_per_month
    return result

print(solution())