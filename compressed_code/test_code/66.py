def solution():
    
    base_salary = 500
    overtime_salary = 20
    regular_hours = 40
    overtime_hours = 50 - regular_hours
    total_salary = base_salary + (overtime_salary * overtime_hours)
    result = total_salary
    return result

print(solution())