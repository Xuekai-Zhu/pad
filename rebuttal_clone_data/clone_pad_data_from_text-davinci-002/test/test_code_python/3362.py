def solution():
    coffee_time = 5
    status_time = 2
    payroll_time = 3
    employees = 9
    total_time = coffee_time + status_time * employees + payroll_time * employees
    result = total_time
    return result

print(solution())