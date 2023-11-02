def solution():
    """Out of 480 employees, 10% got a salary increase while 20% got a travel allowance increase. How many employees did not get any increase?"""
    total_employees = 480
    salary_increase_percent = 10
    travel_allowance_increase_percent = 20
    num_salary_increase = total_employees * (salary_increase_percent / 100)
    num_travel_allowance_increase = total_employees * (travel_allowance_increase_percent / 100)
    num_no_increase = total_employees - num_salary_increase - num_travel_allowance_increase
    result = num_no_increase
    return result

print(solution())